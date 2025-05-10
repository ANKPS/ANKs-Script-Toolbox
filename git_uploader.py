""" *** DOC STRING *** """
import logging
import subprocess

#region Logger

logger = logging.getLogger("GitCommitHandler")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(LOG_FORMAT)
ch.setFormatter(formatter)

logger.addHandler(ch)

#endregion

class GitCommitHandler:
    """ *** MODULE DOC STRING *** """
    def __init__(self, branch_name = None, commit_message = None):
        self.branch_name = branch_name or self.get_branch_name()
        self.commit_message = commit_message or "Automated Commit"

        self.commands = [
            ["git", "add", "."],
            ["git", "commit", "-m", self.commit_message],
            ["git", "push", "origin", self.branch_name]
        ]

    @staticmethod
    def get_branch_name():
        """ *** DOC STRING *** """
        try:
            branch = subprocess.check_output([
                "git",
                "rev-parse",
                "--abbrev-ref",
                "HEAD"
            ], stderr=subprocess.DEVNULL).strip().decode("utf-8")

            return branch
        except subprocess.CalledProcessError:
            return None

    def handle_commit(self):
        """ *** DOC STRING *** """
        try:
            for command in self.commands:
                logger.info("Executing command: %s", command)
                result = subprocess.run(command, shell=True)

                if result.returncode != 0:
                    logger.info("Command failed: %s", command)
                    break

            logger.info("Successfully committed and pushed changes.")
        except subprocess.CalledProcessError as e:
            logger.info("Error executing command: %s", e)
        except FileNotFoundError:
            logger.info("Error: Command not found"
                        "Make sure Git is installed and added to your PATH.")

if __name__ == "__main__":
    commit_input = input("Enter commit message (or leave blank for default): ")

    gch = GitCommitHandler(commit_message = commit_input)

    gch.handle_commit()
