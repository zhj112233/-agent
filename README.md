智能简历优化 Agent
基于 DeepSeek 大模型的简历优化智能体应用，帮助求职者快速分析简历与目标岗位的匹配度，输出专业优化建议，并一键生成贴合岗位要求的优化后简历。完整支持 Docker 一键部署，开箱即用。
项目简介
本应用针对求职者简历优化痛点设计，通过大语言模型实现简历与目标岗位 JD 的精准匹配分析，在不虚构经历的前提下，最大化突出简历与岗位的匹配亮点，补齐表述缺口，生成专业、规范的求职简历。全程无用户数据持久化存储，保障隐私安全。
功能特性
📄 支持简历内容与目标职位描述（JD）的自由文本输入，兼容 Markdown 格式简历
🔍 智能多维度匹配分析，精准输出匹配亮点、核心能力缺口、可落地优化建议
✨ 一键生成优化后的完整简历，保留真实经历的同时，最大化贴合岗位招聘要求
📥 支持优化简历的 Markdown 格式一键导出，可直接复制到简历编辑器使用
🐳 完整支持 Docker 容器化构建与部署，无需配置本地 Python 环境，开箱即用
🔒 全流程内存级数据处理，不持久化存储任何用户输入的简历、JD 内容，保障隐私安全
环境要求
表格
部署方式	核心要求
Docker 部署（推荐）	Docker Desktop / Docker Engine 20.10+
本地开发运行	Python 3.10+、pip 包管理器
通用必备项	有效的 DeepSeek API Key（需通过环境变量配置，严禁硬编码）
快速开始
前置配置：设置 API Key（必做）
严格遵循任务要求，API Key 仅通过系统环境变量传入，禁止硬编码到代码或配置文件中。
根据你的操作系统，在终端执行对应命令设置环境变量：
bash
运行
# Windows PowerShell
$env:DEEPSEEK_API_KEY="你的DeepSeek_API_Key"

# macOS / Linux
export DEEPSEEK_API_KEY="你的DeepSeek_API_Key"
Docker 一键部署（推荐，开箱即用）
在项目根目录（包含 Dockerfile 的文件夹），依次执行以下命令即可完成部署：
bash
运行
# 1. 构建 Docker 镜像
docker build -t resume-optimizer .

# 2. 启动容器服务（Windows PowerShell）
docker run -d -p 8501:8501 -e DEEPSEEK_API_KEY=$env:DEEPSEEK_API_KEY --name resume-optimizer resume-optimizer

# 2. 启动容器服务（macOS / Linux）
docker run -d -p 8501:8501 -e DEEPSEEK_API_KEY="${DEEPSEEK_API_KEY}" --name resume-optimizer resume-optimizer
服务启动成功后，打开浏览器访问 http://localhost:8501 即可使用应用。
本地开发运行
无需 Docker，直接在本地 Python 环境中运行，步骤如下：
bash
运行
# 1. 克隆/下载项目到本地，进入项目根目录
cd resume-optimizer

# 2. 安装 Python 依赖
pip install -r requirements.txt

# 3. 参考前置配置步骤，设置 DEEPSEEK_API_KEY 环境变量

# 4. 启动应用服务
streamlit run app/main.py
应用启动后会自动打开浏览器，若未自动跳转，手动访问 http://localhost:8501 即可。
使用指南
输入简历内容：在页面左侧文本框，粘贴你的完整简历内容，支持 Markdown 格式排版
输入目标岗位 JD：在页面右侧文本框，粘贴目标岗位的完整职位描述与任职要求
匹配度分析：点击「🔍 分析匹配度」按钮，等待大模型生成完整的匹配分析报告
生成优化简历：确认分析结果后，点击「✨ 生成优化简历」按钮，一键生成贴合岗位要求的优化后简历
导出结果：点击「📥 下载优化简历 (Markdown)」按钮，将优化后的简历保存到本地
项目结构
text
resume-optimizer/
├── app/
│   ├── main.py          # Streamlit 前端主应用，核心交互逻辑实现
│   └── utils.py         # 工具函数：DeepSeek API 调用、专业分析Prompt生成
├── Dockerfile           # Docker 镜像构建配置文件（基于 Python 3.10 官方镜像）
├── requirements.txt     # Python 依赖包清单
└── README.md            # 项目说明文档
