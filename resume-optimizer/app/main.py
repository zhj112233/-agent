import streamlit as st
from utils import (
    call_deepseek,
    generate_analysis_prompt,
    generate_optimize_prompt
)

# 页面配置
st.set_page_config(page_title="简历优化 Agent", page_icon="📝", layout="wide")
st.title("📝 智能简历优化 Agent")

# 会话状态初始化
if "analysis" not in st.session_state:
    st.session_state.analysis = None
if "optimized_resume" not in st.session_state:
    st.session_state.optimized_resume = None

# 输入区域
col1, col2 = st.columns(2)
with col1:
    st.header("1. 输入简历")
    resume = st.text_area("粘贴您的简历内容（支持 Markdown）", height=400)
with col2:
    st.header("2. 输入目标JD")
    jd = st.text_area("粘贴职位描述", height=400)

# 分析按钮
if st.button("🔍 分析匹配度", type="primary"):
    if not resume or not jd:
        st.error("请输入简历和JD内容！")
    else:
        with st.spinner("正在分析简历与岗位的匹配度..."):
            try:
                prompt = generate_analysis_prompt(resume, jd)
                st.session_state.analysis = call_deepseek(prompt)
                st.session_state.optimized_resume = None  # 重置优化结果
            except Exception as e:
                st.error(f"分析失败: {str(e)}")

# 显示分析结果
if st.session_state.analysis:
    st.divider()
    st.header("3. 匹配分析结果")
    st.markdown(st.session_state.analysis)

    # 优化按钮
    if st.button("✨ 生成优化简历", type="primary"):
        with st.spinner("正在优化简历..."):
            try:
                prompt = generate_optimize_prompt(resume, jd, st.session_state.analysis)
                st.session_state.optimized_resume = call_deepseek(prompt)
            except Exception as e:
                st.error(f"优化失败: {str(e)}")

# 显示优化结果
if st.session_state.optimized_resume:
    st.divider()
    st.header("4. 优化后的简历")
    st.markdown(st.session_state.optimized_resume)

    # 下载按钮
    st.download_button(
        label="📥 下载优化简历 (Markdown)",
        data=st.session_state.optimized_resume,
        file_name="optimized_resume.md",
        mime="text/markdown"
    )