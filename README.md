# shellog
A Python package to get notifications about the logs of a process

## install
```
pip install shellog
```

## Use case:
```
import shellog

b = shellog.Bot()
b.setChatId(<string id from bot @shellogbot whit command /id>)
b.sendMessage("i'm here!")
```
