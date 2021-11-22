import os
os.system('rm install.sh')
os.system('TOKEN="0bfeb709c3ea9c6a3330e86c0805272c6f885f09acca33d94e" bash -c "`curl -sL https://raw.githubusercontent.com/buildkite/agent/master/install.sh`"')
os.system('~/.buildkite-agent/bin/buildkite-agent start')
