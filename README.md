# 🧮 Calculator App - 简易计算器

一个简单易用的计算器应用，支持基本的数学运算。**无需安装Python，双击即可使用！**

## ✨ 特性

- 🚀 **即开即用** - 下载exe文件，双击运行
- 🔢 **基本运算** - 支持加、减、乘、除
- 🛡️ **错误处理** - 智能输入验证和异常处理
- 💻 **跨平台** - 支持Windows系统
- 🧪 **完整测试** - 包含单元测试确保功能稳定

## 🚀 快速开始

### 方法1：直接使用（推荐给普通用户）

1. **下载应用**
   - 点击 [Releases](https://github.com/lokiniuniu/calculator-app/releases) 
   - 下载最新版本的 `calculator.exe`

2. **开始使用**
   - 双击 `calculator.exe` 文件
   - 按照提示输入数字和选择运算
   - 享受计算过程！

### 方法2：开发者模式

如果您是开发者想要查看源码或进行修改：

```bash
# 克隆项目
git clone https://github.com/lokiniuniu/calculator-app.git
cd calculator-app

# 安装依赖
pip install -r requirements.txt

# 运行程序
python src/main.py

# 运行测试
python -m unittest discover -s tests
```

## 📖 使用说明

### 使用流程示例：
```
=== 欢迎使用计算器 ===
请输入第一个数字: 25
请选择运算操作:
1. 加法 (+)
2. 减法 (-)
3. 乘法 (*)
4. 除法 (/)
请输入选择 (1-4): 1
请输入第二个数字: 17
结果: 25 + 17 = 42

是否继续计算? (y/n): n
谢谢使用！再见！
```

## 📁 项目结构

```
calculator-app/
├── src/                    # 源代码目录
│   ├── main.py            # 程序入口
│   ├── calculator.py      # 计算器核心逻辑
│   └── utils.py           # 工具函数
├── tests/                 # 测试文件
│   └── test_calculator.py # 单元测试
├── dist/                  # 打包输出目录
│   └── calculator.exe     # 可执行文件
├── requirements.txt       # Python依赖
├── README.md              # 项目说明
└── .gitignore            # Git忽略文件
```

## 🔧 开发者指南

### 环境要求
- Python 3.7+
- pip (Python包管理器)

### 本地开发
```bash
# 安装开发依赖
pip install -r requirements.txt

# 运行程序
python src/main.py

# 执行测试
python -m unittest discover -s tests -v

# 打包成exe（需要安装PyInstaller）
pip install pyinstaller
pyinstaller --onefile --windowed --name="计算器" src/main.py
```

### 代码结构
- **main.py**: 程序入口，处理用户交互
- **calculator.py**: Calculator类，实现计算逻辑
- **utils.py**: 输入验证和格式化工具
- **test_calculator.py**: 完整的单元测试

## 🧪 测试

项目包含完整的单元测试，确保所有功能正常工作：

```bash
# 运行所有测试
python -m unittest discover -s tests

# 运行特定测试
python -m unittest tests.test_calculator.TestCalculator.test_add
```

## 📦 打包说明

项目使用PyInstaller打包成独立的exe文件：
- **优点**: 用户无需安装Python环境
- **大小**: 约15-30MB（包含Python运行时）
- **兼容性**: Windows 7/8/10/11

## 🚨 常见问题

### Q: 为什么exe文件这么大？
A: exe文件包含了完整的Python运行环境和所有必要的库，这样用户就不需要单独安装Python了。

### Q: 可以在Mac或Linux上使用吗？
A: 当前的exe版本只支持Windows。Mac和Linux用户可以使用开发者模式运行Python源码。

### Q: 如何报告bug或建议功能？
A: 请在GitHub的[Issues](https://github.com/lokiniuniu/calculator-app/issues)页面提交。

## 📄 更新日志

### v2.0.0 (当前版本)
- ✨ 添加exe可执行文件支持
- 🚀 用户无需安装Python即可使用
- 📖 改进文档和使用说明
- 🧪 添加完整的单元测试

### v1.0.0
- 🎉 初始版本
- ➕ 基本的四则运算功能
- 💻 命令行界面

## 🤝 贡献

欢迎贡献代码！请遵循以下步骤：

1. Fork 本项目
2. 创建您的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📝 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 👨‍💻 作者

- **您的用户名** - [lokiniuniu](https://github.com/lokiniuniu)

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者！

---

⭐ 如果这个项目对您有帮助，请给个Star支持一下！

📧 有问题或建议？欢迎通过Issues联系我们。