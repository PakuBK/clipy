from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.padding import Padding
from rich.markdown import Markdown
from rich.prompt import Prompt, Confirm
import os

console = Console()

def print_title(text):
    panel = Panel(Text(text, justify="center", style="magenta bold"), subtitle="by Paku", expand=False)
    console.print(panel)

def print_step(text):
    panel = Panel(text, expand=False)
    console.print(panel)

def print_markdown(text):
    """Prints a rich info message. Support Markdown syntax."""
    md = Padding(Markdown(text), 2)
    console.print(md)

def print_substep(text, style=""):
    """Prints a rich info message without the panelling."""
    console.print("[bright_black]" + text, style=style)

def ask_user(question, default=None):
    answer = Prompt.ask("[green]"+question, default=default)
    return answer

def confirm_by_user(question, color="cyan"):
    answer = Confirm.ask(f"[{color}]"+question+f"[/{color}]")
    return answer

def clear_console():
    os.system("cls")

def print_error(text):
    console.print(Panel("[red]"+text+"[/red]"))