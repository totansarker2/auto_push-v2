1. Place auto_push to your project directory
2. change your git_home_path and watch_dog_path.
3. Do not put watch_path and git_home_path in same directory, that cause infinite loop!!!

default path is:
git_home_path = "../career_hub"
watch_path = "../career_hub/src"
script_path = "../auto_push/script.sh"
sleep_time = ""

# next feature coming:
1. user can give there own path to source_path and sleep_time
- main.py will read the path and send that to watchdog