import disnake
from disnake.ext import commands
import execjs
import io
import sys

class CodeExecutor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="run_code", description="Run code in the given language (python, js, html, css)")
    async def run_code(self, inter: disnake.ApplicationCommandInteraction, 
                       lang: str, 
                       code: str):
        """Run code in the given language (python, js, html, css)."""
        
        # Handle Python execution
        if lang == "python":
            try:
                # Redirect stdout to capture print statements
                old_stdout = sys.stdout
                sys.stdout = io.StringIO()

                exec_locals = {}
                exec(code, {}, exec_locals)

                # Capture the result from stdout (print statements)
                result = sys.stdout.getvalue() + "\n"

                # Include any variables in exec_locals
                for key, value in exec_locals.items():
                    result += f"{key}: {value}\n"

                sys.stdout = old_stdout  # Reset stdout

                if not result:
                    result = "No output produced."

                if len(result) > 2000:
                    result = result[:2000]  # Truncate if too long

                await inter.response.send_message(f"Execution result (Python):\n{result}")
            except Exception as e:
                await inter.response.send_message(f"Error running Python code: {str(e)}")

        # Handle JavaScript execution
        elif lang == "javascript":
            try:
                ctx = execjs.compile("""
                function run(code) {
                    return eval(code);
                }
                """)
                result = ctx.call("run", code)
                await inter.response.send_message(f"Execution result (JavaScript):\n{result}")
            except Exception as e:
                await inter.response.send_message(f"Error running JavaScript code: {str(e)}")

        # Handle HTML/CSS (just return the code)
        elif lang == "html" or lang == "css":
            await inter.response.send_message(f"Execution result (HTML/CSS):\n```{code}```")

        else:
            await inter.response.send_message("Supported languages are: python, javascript, html, css.")

def setup(bot):
    bot.add_cog(CodeExecutor(bot))
