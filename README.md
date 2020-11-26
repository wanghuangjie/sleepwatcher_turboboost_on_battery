# sleepwatcher_turboboost_on_battery
关闭turboboost，当使用电池时


1. ```brew cask install sleepwatcher```
2. ```brew services start sleepwatcher```
3. ```mkdir -p ~/code/python/utils/```
4. ```wget -P ~/code/python/utils/ https://raw.githubusercontent.com/wanghuangjie/sleepwatcher_turboboost_on_battery/master/boostoff_battery.py```
5. ```wget -P ~ -O .wakeup https://raw.githubusercontent.com/wanghuangjie/sleepwatcher_turboboost_on_battery/master/wakeup```
6. ```chmod 755 ~/.wakeup```
7. sudo visudo 添加到最底部
   ```%admin ALL=(root) NOPASSWD: /Applications/Utilities/voltageshift/voltageshift```


睡眠再唤醒，如未接电源，应有关闭turbo_boost的提示。
