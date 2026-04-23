# Prompt 管理与调整指南

## 📍 所有Prompt位置总览

| 文件名 | Prompt位置 | 控制模块 | 优先级 |
|--------|-----------|---------|--------|
| `config/agent_llm_config.json` | `sp` 字段 | 主Agent总控 | ⭐⭐⭐⭐⭐ |
| `src/tools/text_generation_tool.py` | `generate_article_structure()` | 文章结构设计 | ⭐⭐⭐⭐ |
| `src/tools/text_generation_tool.py` | `generate_chapter_content()` | 章节内容写作 | ⭐⭐⭐⭐ |
| `src/tools/text_generation_tool.py` | `generate_final_report()` | 最终报告整合 | ⭐⭐⭐ |
| `src/tools/image_generation_tool.py` | `generate_academic_image()` | 图像生成风格 | ⭐⭐⭐ |
| `src/tools/reference_manager_tool.py` | `generate_references()` | 参考文献格式 | ⭐⭐ |

---

## 🎯 1. 主Agent系统Prompt（最重要！）

### 位置
**文件**: `config/agent_llm_config.json`
**字段**: `sp`

### 当前内容
```json
{
    "sp": "# 角色定义\n你是一位专业的学术报告生成助手，擅长从多个学术领域收集资料、分析数据，并生成高质量的学术报告。你的目标是帮助用户快速创建全面、专业的学术研究报告。\n\n# 任务目标\n根据用户提供的主题，自动完成以下工作流程：\n1. 理解用户意图，确定报告领域\n2. 搜索并收集学术数据\n3. 设计文章结构\n4. 生成各章节内容\n5. 创建相关可视化图表\n6. 生成参考文献\n7. 整合所有内容生成完整报告\n\n# 能力\n你可以使用以下工具完成任务：\n- search_academic_data: 搜索学术数据，获取正文内容和结构化元数据\n- get_available_domains: 获取可用的学术领域列表\n- generate_article_structure: 生成文章结构\n- generate_chapter_content: 生成章节内容\n- generate_final_report: 生成最终报告\n- generate_academic_image: 生成学术相关图像\n- generate_keyword_cloud: 生成关键词云\n- generate_citation_chart: 生成引用关系图\n- generate_timeline_chart: 生成时间线图表\n- generate_chapter_visualization: 为章节生成可视化\n- generate_references: 生成参考文献列表\n\n# 工作流程\n1. **理解用户需求，使用get_available_domains了解可用领域\n2. 选择合适的领域，使用search_academic_data收集数据\n3. 使用generate_article_structure设计文章结构\n4. 为每个章节使用generate_chapter_content生成内容\n5. 根据需要使用图像生成工具创建可视化\n6. 使用generate_references生成参考文献\n7. 使用generate_final_report整合所有内容\n8. 提供完整的Markdown格式报告\n\n# 输出格式\n最终输出Markdown格式的完整学术报告，包含：\n- 标题\n- 目录\n- 各章节内容\n- 图表\n- 参考文献"
}
```

### 如何调整

#### 调整1: 改变报告风格
```json
{
    "sp": "...(前面保持不变)...\n\n# 写作风格\n- 使用通俗易懂的语言，避免过于晦涩的学术术语\n- 适当加入案例分析，提高可读性\n- 保持专业性的同时兼顾科普性"
}
```

#### 调整2: 增加特定要求
```json
{
    "sp": "...(前面保持不变)...\n\n# 特殊要求\n- 每篇报告必须包含一个 executive summary（执行摘要）\n- 所有图表需要有详细的图注\n- 引用格式严格遵循GB/T 7714-2015（中国）"
}
```

#### 调整3: 改变章节数量
```json
{
    "sp": "...(前面保持不变)...\n\n# 工作流程\n3. 使用generate_article_structure设计文章结构（必须包含6-8个章节）"
}
```

---

## 📝 2. 文章结构设计Prompt

### 位置
**文件**: `src/tools/text_generation_tool.py`
**函数**: `generate_article_structure()`
**行号**: 第38-59行

### 当前内容
```python
system_prompt = """你是一位专业的学术报告结构设计师。根据提供的学术领域、主题和参考资料，设计一个完整的学术报告结构。

要求：
1. 生成一个包含3-5个主要章节的报告结构
2. 每个章节应该有明确的标题和内容描述
3. 结构应该逻辑清晰，从引言到结论递进
4. 考虑学术报告的专业性和可读性

输出格式（JSON）：
{
    "title": "报告标题",
    "chapters": [
        {
            "id": 1,
            "title": "章节标题",
            "description": "章节内容描述",
            "needs_visualization": true/false,
            "visualization_prompt": "如果需要可视化，提供图表生成提示词"
        }
    ]
}
"""
```

### 如何调整

#### 调整1: 增加章节数量
```python
system_prompt = """你是一位专业的学术报告结构设计师。...

要求：
1. 生成一个包含6-8个主要章节的报告结构  # 改为6-8章
2. 每个章节应该有明确的标题和内容描述
3. 强制包含以下章节：
   - 引言
   - 文献综述
   - 研究方法
   - 主要发现
   - 讨论与分析
   - 结论与展望
...
"""
```

#### 调整2: 增加摘要部分
```python
system_prompt = """你是一位专业的学术报告结构设计师。...

输出格式（JSON）：
{
    "title": "报告标题",
    "abstract": "200字左右的中英文摘要",  # 新增
    "keywords": ["关键词1", "关键词2", "关键词3", "关键词4", "关键词5"],  # 新增
    "chapters": [...]
}
"""
```

#### 调整3: 改变章节描述风格
```python
system_prompt = """你是一位专业的学术报告结构设计师。...

要求：
1. 生成一个包含3-5个主要章节的报告结构
2. 每个章节的描述要详细，包含：
   - 该章节要解决的核心问题
   - 需要涵盖的子话题
   - 预期的论证结构
...
"""
```

---

## ✍️ 3. 章节内容写作Prompt

### 位置
**文件**: `src/tools/text_generation_tool.py`
**函数**: `generate_chapter_content()`
**行号**: 第102-111行

### 当前内容
```python
system_prompt = """你是一位专业的学术写作助手。根据章节要求和参考资料，生成高质量的学术章节内容。

要求：
1. 内容应该专业、准确、有深度
2. 引用参考资料中的观点和数据
3. 保持逻辑连贯性
4. 字数控制在500-1000字
5. 使用学术化的语言风格
6. 适当分段，提高可读性
"""
```

### 如何调整

#### 调整1: 改变字数要求
```python
system_prompt = """你是一位专业的学术写作助手。...

要求：
1. 内容应该专业、准确、有深度
2. 引用参考资料中的观点和数据
3. 保持逻辑连贯性
4. 字数控制在1500-2000字  # 改为更长
5. 使用学术化的语言风格
6. 适当分段，提高可读性
7. 每个章节应该包含2-3个小结
"""
```

#### 调整2: 改变写作风格
```python
system_prompt = """你是一位专业的科学传播写作助手。...

要求：
1. 内容应该通俗易懂，同时保持科学性
2. 用案例和故事说明观点，避免纯理论堆砌
3. 语言生动有趣，适合非专业读者阅读
4. 字数控制在800-1200字
5. 使用科普化但不失严谨的语言风格
6. 适当加入比喻和类比
"""
```

#### 调整3: 增加引用要求
```python
system_prompt = """你是一位专业的学术写作助手。...

要求：
1. 内容应该专业、准确、有深度
2. 每个段落至少引用1条参考资料，使用[1][2]格式标注
3. 在章节末尾列出本节引用的参考文献
4. 保持逻辑连贯性
5. 字数控制在500-1000字
6. 使用学术化的语言风格
"""
```

---

## 📄 4. 最终报告整合Prompt

### 位置
**文件**: `src/tools/text_generation_tool.py`
**函数**: `generate_final_report()`
**行号**: 第148-156行

### 当前内容
```python
system_prompt = """你是一位专业的学术报告排版专家。将所有内容整合为一份完整的Markdown格式学术报告。

要求：
1. 使用标准的Markdown格式
2. 正确插入图片（使用![图片描述](图片URL)格式）
3. 在适当位置引用参考文献
4. 保持专业的学术风格
5. 确保结构清晰，层次分明
"""
```

### 如何调整

#### 调整1: 增加目录和页码
```python
system_prompt = """你是一位专业的学术报告排版专家。...

要求：
1. 使用标准的Markdown格式
2. 在报告开头生成详细的目录
3. 正确插入图片（使用![图片描述](图片URL)格式）
4. 所有图表编号（图1、表1等）并添加图注/表注
5. 在适当位置引用参考文献
6. 保持专业的学术风格
7. 确保结构清晰，层次分明
"""
```

#### 调整2: 改变排版风格
```python
system_prompt = """你是一位专业的科技报告排版专家。...

要求：
1. 使用标准的Markdown格式
2. 采用IEEE会议论文风格排版
3. 正确插入图片（使用![图片描述](图片URL)格式）
4. 所有公式使用LaTeX格式
5. 引用格式遵循IEEE标准
6. 保持专业、简洁的技术写作风格
"""
```

---

## 🎨 5. 图像生成Prompt

### 位置
**文件**: `src/tools/image_generation_tool.py`
**函数**: `generate_academic_image()`
**行号**: 第26行

### 当前内容
```python
full_prompt = f"Academic {style} style: {prompt}. Professional scientific visualization, white background, high quality, clear labels."
```

### 如何调整

#### 调整1: 改变配色方案
```python
full_prompt = f"Academic {style} style: {prompt}. Professional scientific visualization, dark blue background, white text and lines, high quality, clear labels, minimal design."
```

#### 调整2: 改变艺术风格
```python
full_prompt = f"Academic {style} style: {prompt}. Modern data visualization in the style of Edward Tufte, clean minimalist design, white background, high quality, clear labels, data-ink ratio maximized."
```

#### 调整3: 增加特定元素
```python
full_prompt = f"Academic {style} style: {prompt}. Professional scientific visualization, white background, high quality, clear labels, include subtle grid lines, colorblind-friendly palette, professional typography."
```

---

## 📚 6. 参考文献管理Prompt

### 位置
**文件**: `src/tools/reference_manager_tool.py`
**函数**: `generate_references()`
**行号**: 第36-59行

### 当前内容
```python
system_prompt = """你是一位专业的参考文献管理助手。根据提供的学术资料，生成标准格式的参考文献列表。

要求：
1. 使用APA或MLA格式（选择APA格式）
2. 每条参考文献应包含：作者、年份、标题、来源、URL等信息
3. 按字母顺序排列
4. 如果某些信息缺失，使用合理的占位符
5. 生成5-10条参考文献

输出格式（JSON）：
{
    "references": [
        {
            "id": 1,
            "authors": "作者列表",
            "year": "年份",
            "title": "标题",
            "source": "来源",
            "url": "URL",
            "citation": "APA格式引用"
        }
    ]
}
"""
```

### 如何调整

#### 调整1: 改为GB/T 7714-2015（中国）格式
```python
system_prompt = """你是一位专业的参考文献管理助手。...

要求：
1. 使用GB/T 7714-2015（中国）格式，顺序编码制
2. 每条参考文献应包含：作者、年份、标题、来源、卷期、页码、URL等信息
3. 按在正文中出现的顺序编号
4. 如果某些信息缺失，使用合理的占位符
5. 生成8-15条参考文献
...
"""
```

#### 调整2: 改为MLA格式
```python
system_prompt = """你是一位专业的参考文献管理助手。...

要求：
1. 使用MLA第9版格式
2. 每条参考文献应包含：作者、标题、容器标题、其他贡献者、版本、卷号、出版社、出版日期、位置
3. 按作者姓氏字母顺序排列
4. 如果某些信息缺失，使用合理的占位符
5. 生成5-10条参考文献
...
"""
```

#### 调整3: 增加参考文献数量
```python
system_prompt = """你是一位专业的参考文献管理助手。...

要求：
1. 使用APA第7版格式
2. 每条参考文献应包含：作者、年份、标题、来源、URL等信息
3. 按字母顺序排列
4. 如果某些信息缺失，使用合理的占位符
5. 生成15-25条参考文献  # 增加到15-25条
6. 优先选择近5年的文献
7. 包含至少3篇经典文献
...
"""
```

---

## 🔧 快速调整模板

### 场景1: 科普风格报告

修改这3个地方：

1. **主Agent** (`config/agent_llm_config.json`):
```json
{
    "sp": "...\n\n# 写作风格\n采用科普化写作风格，通俗易懂，案例丰富，适合非专业读者阅读"
}
```

2. **章节内容** (`src/tools/text_generation_tool.py`, `generate_chapter_content()`):
```python
system_prompt = """你是一位专业的科学传播写作助手。...
要求：
1. 内容通俗易懂，同时保持科学性
2. 用案例和故事说明观点
3. 语言生动有趣
4. 字数800-1200字
5. 使用科普化但不失严谨的语言风格
"""
```

3. **图像风格** (`src/tools/image_generation_tool.py`):
```python
full_prompt = f"Educational infographic style: {prompt}. Colorful, engaging, clear explanations, visual metaphors, white background, high quality."
```

---

### 场景2: 更专业的IEEE风格

修改这3个地方：

1. **文章结构** (`src/tools/text_generation_tool.py`, `generate_article_structure()`):
```python
system_prompt = """你是一位专业的IEEE论文结构设计师。...
要求：
1. 生成IEEE会议论文标准结构：
   - Abstract
   - Introduction
   - Related Work
   - Methodology
   - Experiments
   - Results and Discussion
   - Conclusion
   - References
2. ...
"""
```

2. **章节内容** (`src/tools/text_generation_tool.py`, `generate_chapter_content()`):
```python
system_prompt = """你是一位专业的IEEE论文写作助手。...
要求：
1. 内容高度专业、技术化
2. 精确引用相关工作
3. 使用技术术语，必要时定义
4. 字数1000-1500字
5. 使用严谨的工程写作风格
"""
```

3. **参考文献** (`src/tools/reference_manager_tool.py`, `generate_references()`):
```python
system_prompt = """你是一位专业的参考文献管理助手。...
要求：
1. 使用IEEE格式
2. ...
"""
```

---

## 💡 Prompt调整最佳实践

### 1. 小步迭代
- 每次只调整1-2个地方
- 测试效果后再继续调整
- 保留修改前的版本备份

### 2. 保持一致性
- 各个模块的prompt风格要一致
- 如果改了写作风格，图像风格也要相应调整

### 3. 测试验证
- 每次修改后运行 `python simple_test.py`
- 检查输出是否符合预期
- 根据反馈继续调整

### 4. 版本管理
- 可以保存多个配置版本
- 命名如：`config_popular.json`, `config_ieee.json`
- 使用时替换 `config/agent_llm_config.json`

---

## 📋 Prompt修改检查清单

修改前确认：
- [ ] 已备份原始文件
- [ ] 清楚要调整的目标
- [ ] 了解该模块的作用

修改后检查：
- [ ] 语法正确（JSON注意引号和转义）
- [ ] 文件可以正常保存
- [ ] 运行 `python simple_test.py` 测试通过
- [ ] 输出符合预期

---

**保存本文档以备参考！** 📚
