<!-- markdownlint-disable MD033 MD036 MD041 MD045 -->
<div align="center">
  <a href="https://v2.nonebot.dev/store">
    <img src="./docs/NoneBotPlugin.svg" width="300" alt="logo">
  </a>

</div>

<div align="center">

# NoneBot-Plugin-LLM-Extension

_✨ 将自然语言转换为机器人指令 ✨_

<a href="">
  <img src="https://img.shields.io/pypi/v/nonebot-plugin-llm-extension.svg" alt="pypi" />
</a>
<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">
<a href="https://github.com/astral-sh/uv">
  <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv-managed">
</a>
<a href="https://github.com/nonebot/plugin-alconna">
  <img src="https://img.shields.io/badge/Alconna-resolved-2564C2" alt="alc-resolved">
</a>

<br/>

<a href="https://registry.nonebot.dev/plugin/nonebot-plugin-llm-enxtension:nonebot_plugin_llm_enxtension">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin%2Fnonebot-plugin-llm-enxtension" alt="NoneBot Registry" />
</a>
<a href="https://registry.nonebot.dev/plugin/nonebot-plugin-llm-enxtension:nonebot_plugin_llm_enxtension">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin-adapters%2Fnonebot-plugin-llm_enxtension" alt="Supported Adapters" />
</a>

<br />
<a href="#-效果图">
  <strong>📸 演示与预览</strong>
</a>
&nbsp;&nbsp;|&nbsp;&nbsp;
<a href="#-安装">
  <strong>📦️ 下载插件</strong>
</a>
&nbsp;&nbsp;|&nbsp;&nbsp;
<a href="https://qm.qq.com/q/Vuipof2zug" target="__blank">
  <strong>💬 加入交流群</strong>
</a>

</div>

## 📖 介绍 <img src="https://raw.githubusercontent.com/fenxer/llm-things/3eaaba79ddf48a784304493adfbaa614f410d6e6/images/human-coded.svg" width="100" alt="Human coded" />

利用 LLM 将自然语言转换为机器人指令 / Convert natural language messages into bot commands using LLMs

> [!IMPORTANT]
> **收藏项目**，你将从 GitHub 上无延迟地接收所有发布通知～⭐️

<img width="100%" src="https://starify.komoridevs.icu/api/starify?owner=KomoriDev&repo=nonebot-plugin-llm-extension" alt="starify" />

<!-- <details>
  <summary><kbd>Star History</kbd></summary>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=KomoriDev/nonebot-plugin-llm-extension&theme=dark&type=Date" />
    <img width="100%" src="https://star-history.com/#KomoriDev/nonebot-plugin-llm-extension&Date" />
  </picture>
</details> -->

## 💿 安装

以下提到的方法任选 **其一** 即可

<details open>
<summary>[推荐] 使用 nb-cli 安装</summary>
在 Bot 的根目录下打开命令行, 输入以下指令即可安装

```bash
nb plugin install nonebot-plugin-llm-extension
```

</details>
<details>
<summary>使用包管理器安装</summary>

```bash
pip install nonebot-plugin-llm-extension
# or, use poetry
poetry add nonebot-plugin-llm-extension
# or, use pdm
pdm add nonebot-plugin-llm-extension
# or, use uv
uv add nonebot-plugin-llm-extension
```

</details>

## ⚙️ 配置

在项目的配置文件中添加下表中配置：

~~其实这里并不建议使用 deepseek~~

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| llm_extension__api_key | 无 | API 密钥 |
| llm_extension__base_url | <https://api.deepseek.com/v1> | API 端点 |
| llm_extension__model | deepseek-reasoner | 模型名 |

## 🎉 使用

> [!NOTE]
> 为了使 LLM 能够更好地理解和转换用户输入为指令，建议在构造指令时：
>
> 1. **完善命令描述**：为每个命令提供清晰、准确的描述信息
> 2. **丰富参数说明**：详细说明每个参数的含义、类型和取值范围
> 3. **提供使用示例**：给出具体的操作示例，帮助 LLM 理解命令的使用场景

```py
from nonebot_plugin_llm_extension import LLMExtension
from nonebot_plugin_alconna import on_alconna, Args, Alconna, CommandMeta

weather = on_alconna(
    Alconna(
      "weather",
      Args["location?#地区", str],
      meta=CommandMeta(
        description="今日天气",
        example="/天气 陕西汉中"
      )
    ), 
    use_cmd_start=True,
    extension=[LLMExtension],
)
```

通过提供完善的命令元信息，可以让 LLM 更准确地理解命令意图，从而提高自然语言到指令的转换准确率

## 📸 效果图

~~理论上，这里应该有一张图片~~

## 💖 鸣谢

- [`KomoriDev/Starify`](https://github.com/KomoriDev/Starify)：提供了引人注目的徽章

## 📄 许可证

本项目使用 MIT 许可证开源

```txt
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
