# 智能简历优化 Agent
基于 DeepSeek 大模型的简历优化智能体应用，帮助求职者快速分析简历与目标岗位的匹配度，输出专业优化建议，并一键生成贴合岗位要求的优化后简历。完整支持 Docker 一键部署，开箱即用。

## 功能特性
- 📄 支持简历内容与目标职位描述（JD）的文本输入
- 🔍 智能匹配分析，精准输出**匹配亮点**、**核心缺口**、**可落地优化建议**
- ✨ 一键生成优化后的完整简历，保留真实经历的同时最大化贴合岗位要求
- 📥 支持优化简历的 Markdown 格式导出
- 🐳 完整支持 Docker 容器化构建与部署
- 🔒 无数据存储，所有内容仅在内存中处理，保障隐私安全

## 环境要求
- **推荐部署方式**：Docker Desktop / Docker Engine（无需额外配置Python环境）
- **本地开发方式**：Python 3.10+、pip 包管理器
- **必备项**：DeepSeek API Key（需自行配置，严禁硬编码）

## 快速开始
### Docker 部署
 1. 配置环境变量
**必须**通过环境变量传入 DeepSeek API Key，严禁写在命令行历史或配置文件中。
```bash
# Windows PowerShell
$env:DEEPSEEK_API_KEY="你的DeepSeek_API_Key"

# macOS / Linux
export DEEPSEEK_API_KEY="你的DeepSeek_API_Key"

 2. 构建 Docker 镜像
在项目根目录（包含 Dockerfile 的文件夹）执行：
bash
运行
docker build -t resume-optimizer .
3. 启动服务
bash
运行
# Windows PowerShell
docker run -d -p 8501:8501 -e DEEPSEEK_API_KEY=`$env:DEEPSEEK_API_KEY --name resume-optimizer resume-optimizer

# macOS / Linux
docker run -d -p 8501:8501 -e DEEPSEEK_API_KEY="${DEEPSEEK_API_KEY}" --name resume-optimizer resume-optimizer
4. 访问应用
打开浏览器，访问地址即可使用：
plaintext
http://localhost:8501
