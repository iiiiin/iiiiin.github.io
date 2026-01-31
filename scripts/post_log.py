import os
import subprocess
import sys
import datetime
import json
import google.generativeai as genai
from dotenv import load_dotenv

# --- [설정 구간] ---
# .env 파일 로드
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
load_dotenv(os.path.join(root_dir, '.env'))

# Gemini API 설정
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") 
if not GOOGLE_API_KEY:
    print("❌ 에러: .env 파일에서 GOOGLE_API_KEY를 찾을 수 없습니다.")
    sys.exit(1)

genai.configure(api_key=GOOGLE_API_KEY)

# 감시할 로컬 리포지토리 목록
TARGET_REPOS = [
    "/Users/iiiiin/WIP/dev-log-hub",
    "/Users/iiiiin/WIP/turtleneck-macos",
    "/Users/iiiiin/WIP/turtleneck-extension",
    "/Users/iiiiin/WIP/my-dear-extension",
    "/Users/iiiiin/WIP/a-cup-of",
    "/Users/iiiiin/WIP/hop-account",
    "/Users/iiiiin/WIP/cocos-forest",
    "/Users/iiiiin/WIP/portfolio",
]
# ------------------

def get_git_changes(repo_path):
    """특정 리포지토리의 오늘 변경사항을 가져옵니다."""
    try:
        if not os.path.exists(repo_path):
            return None

        # 1. 오늘 자정 이후 커밋
        logs = subprocess.check_output(
            ['git', 'log', '--since=midnight', '--pretty=format:- %s'], 
            cwd=repo_path, text=True, stderr=subprocess.DEVNULL
        ).strip()

        # 2. 스테이징된 변경사항 (Diff)
        diff = subprocess.check_output(
            ['git', 'diff', '--cached', '.', ':(exclude)package-lock.json', ':(exclude)*.lock'], 
            cwd=repo_path, text=True, stderr=subprocess.DEVNULL
        ).strip()

        if not logs and not diff:
            return None
            
        return {"name": os.path.basename(repo_path), "logs": logs, "diff": diff}

    except Exception:
        return None

def generate_content_with_gemini(project_data):
    """Gemini API를 호출하여 블로그 내용을 생성합니다."""
    print("🤖 AI(Gemini)가 회고록을 작성 중입니다...")
    
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
    당신은 전문 테크니컬 라이터입니다.
    아래 제공된 [Git Commit Log]와 [Code Diff]를 분석하여 개발 일지를 작성해주세요.

    **입력 데이터:**
    - Project: {project_data['project']}
    - Logs: {project_data['logs']}
    - Diff: {project_data['diff']}

    **작성 요구사항:**
    1. **Velog (블로그용):**
       - 개발자들이 읽기 좋게 "문제 해결 과정", "기술적 의사결정", "새로 배운 점" 위주로 상세하게 작성하세요.
       - 제목은 흥미롭고 구체적으로 지어주세요.
       - 한국어로 작성하세요.

    2. **Qiita (일본 기술 블로그용):**
       - Velog 내용과 비슷하되, 일본 개발자 문화에 맞게 정중하고 깔끔한 어조로 작성하세요.
       - 제목을 맨 첫 줄에 적고, 한 줄 띄운 뒤 본문을 작성하세요.
       - 일본어로 작성하세요.

    **출력 형식 (JSON Only):**
    반드시 아래 JSON 포맷으로만 출력하세요. 마크다운 코드 블럭(```json)을 사용하지 말고, 순수 JSON 문자열만 반환하세요.

    {{
      "velog_content": "제목\\n\\n본문...",
      "qiita_content": "제목\\n\\n본문..."
    }}
    """

    try:
        response = model.generate_content(prompt)
        clean_text = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(clean_text)
    except Exception as e:
        print(f"❌ AI 생성 중 오류 발생: {e}")
        return None

def save_to_file(content_json):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. 블로그 파일 생성 (.md)
    blog_filename = f"{today}-dev-log.md"
    blog_path = os.path.join(root_dir, "blog", "_posts", blog_filename)
    
    raw_velog = content_json.get('velog_content', '')
    
    # Velog 내용 처리 (제목 분리 로직 추가)
    if raw_velog:
        v_lines = raw_velog.split('\n')
        # AI가 지어준 제목을 사용하려면 아래 v_title을 사용, 날짜로 하려면 기존 유지
        # 여기서는 본문 중복을 피하기 위해 첫 줄(제목)을 제거하고 본문만 남깁니다.
        v_body = '\n'.join(v_lines[1:]).strip() if len(v_lines) > 1 else raw_velog
    else:
        v_body = "내용 없음"

    blog_lines = [
        "---",
        f'title: "{today} 개발 일지"',
        f"date: {timestamp}",
        "categories: [DevLog]",
        "tags: [TIL]",
        "---",
        "",
        v_body
    ]
    
    with open(blog_path, "w", encoding="utf-8") as f:
        f.write("\n".join(blog_lines))
    print(f"✅ 블로그 파일 생성 완료: {blog_path}")

    # 2. Qiita (CLI용) 파일 생성
    qiita_content = content_json.get('qiita_content', '')
    
    if qiita_content:
        lines = qiita_content.split('\n')
        raw_title = lines[0].replace('#', '').strip() if lines else f"{today} 개발 일지"
        safe_title = raw_title.replace('"', '\\"') 
        body = '\n'.join(lines[1:]).strip()

        qiita_filename = f"{today}-dev-log.md"
        qiita_path = os.path.join(root_dir, "public", qiita_filename)
        os.makedirs(os.path.dirname(qiita_path), exist_ok=True)

        qiita_lines = [
            "---",
            f'title: "{safe_title}"',
            "tags: [\"DevLog\", \"TIL\"]",
            "private: false",
            f"updated_at: '{timestamp}'",
            "id: null",
            "organization_url_name: null",
            "slide: false",
            "ignorePublish: false",
            "---",
            "",
            body
        ]

        with open(qiita_path, "w", encoding="utf-8") as f:
            f.write("\n".join(qiita_lines))
        print(f"✅ Qiita 파일 생성 완료: {qiita_path}")
    
    # VS Code로 블로그 글 열기
    try: subprocess.call(["code", blog_path])
    except: pass

if __name__ == "__main__":
    print("🔍 여러 프로젝트를 순회하며 오늘의 작업을 수집합니다...")
    
    all_logs = []
    all_diffs = []
    active_projects = []

    for repo in TARGET_REPOS:
        data = get_git_changes(repo)
        if data:
            print(f"  👉 감지됨: {data['name']}")
            active_projects.append(data['name'])
            all_logs.append(f"### 📂 Project: {data['name']}\n{data['logs'] if data['logs'] else '커밋 없음'}")
            all_diffs.append(f"### 📂 Project: {data['name']}\n{data['diff'][:3000]}")

    if not active_projects:
        print("📭 오늘은 감지된 변경사항(Staged or Commited)이 없습니다.")
        sys.exit(0)

    # Gemini에게 보낼 데이터 준비
    project_payload = {
        "logs": "\n\n".join(all_logs),
        "diff": "\n\n".join(all_diffs),
        "project": f"Multi-Repo Work ({', '.join(active_projects)})"
    }

    # AI 호출 및 파일 저장
    result_json = generate_content_with_gemini(project_payload)
    
    if result_json:
        save_to_file(result_json)
        print("\n✨ 모든 작업이 완료되었습니다! 생성된 파일을 확인하고 Push하세요.")
    else:
        print("\n❌ AI 응답을 받지 못해 파일 생성을 실패했습니다.")