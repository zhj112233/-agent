智能简历优化 Agent
基于 DeepSeek 大模型的简历优化智能体应用，帮助求职者快速分析简历与目标岗位的匹配度，输出专业优化建议，并一键生成贴合岗位要求的优化后简历。完整支持 Docker 一键部署，开箱即用。
功能特性
📄 支持简历内容与目标职位描述（JD）的文本输入
🔍 智能匹配分析，精准输出匹配亮点、核心缺口、可落地优化建议
✨ 一键生成优化后的完整简历，保留真实经历的同时最大化贴合岗位要求
📥 支持优化简历的 Markdown 格式导出
🐳 完整支持 Docker 容器化构建与部署
🔒 无数据存储，所有内容仅在内存中处理，保障隐私安全
环境要求
推荐部署方式：Docker Desktop / Docker Engine（无需额外配置 Python 环境）
本地开发方式：Python 3.10+、pip 包管理器
必备项：DeepSeek API Key（需自行配置，严禁硬编码）
快速开始
前置准备：配置 API Key（重要！）
必须通过环境变量传入 DeepSeek API Key，严禁写在代码或命令行历史中。
Windows PowerShell：$env:DEEPSEEK_API_KEY="你的DeepSeek_API_Key"
macOS / Linux：export DEEPSEEK_API_KEY="你的DeepSeek_API_Key"
Docker 部署（推荐）
在项目根目录（包含 Dockerfile 的文件夹）依次执行：
bash
运行
# 1. 构建镜像
docker build -t resume-optimizer .

# 2. 启动服务（Windows PowerShell）
docker run -d -p 8501:8501 -e DEEPSEEK_API_KEY=$env:DEEPSEEK_API_KEY --name resume-optimizer resume-optimizer

# 2. 启动服务（macOS / Linux）
docker run -d -p 8501:8501 -e DEEPSEEK_API_KEY="${DEEPSEEK_API_KEY}" --name resume-optimizer resume-optimizer
启动后打开浏览器访问 http://localhost:8501 即可使用。
本地开发运行
在项目根目录依次执行：
bash
运行
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置 API Key（参考前置准备步骤）

# 3. 启动应用
streamlit run app/main.py
启动后会自动打开浏览器，或手动访问 http://localhost:8501。
使用指南
输入简历：在左侧文本框粘贴你的完整简历内容（支持 Markdown 格式）
输入目标 JD：在右侧文本框粘贴目标岗位的职位描述
匹配度分析：点击「分析匹配度」按钮，等待大模型生成完整的匹配分析报告
生成优化简历：确认分析结果后，点击「生成优化简历」，一键生成贴合岗位要求的优化后简历
导出结果：点击「下载优化简历」按钮，将结果保存为 Markdown 文件
项目结构
plaintext
resume-optimizer/
├── app/
│   ├── main.py          # Streamlit 前端主应用，核心交互逻辑
│   └── utils.py         # 工具函数：DeepSeek API 调用、专业 Prompt 生成
├── Dockerfile           # Docker 镜像构建配置（基于 Python 3.10）
├── requirements.txt     # Python 依赖清单
└── README.md            # 项目说明文档
