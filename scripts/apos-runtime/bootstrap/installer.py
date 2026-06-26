import subprocess


class Installer:

    def install_missing(self, missing_modules):

        for module in missing_modules:
            subprocess.run(
                ["pip", "install", module],
                check=False
            )

        return {"installed": missing_modules}