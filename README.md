# ImgurWallpaper
Forked from https://github.com/MattCairns/ImgurDesktop

Python App that downloads random image from http:/reddit.com/r/wallpapers/new/ and replaces a linux desktop wallpaper every 5 minutes

to install to same directory hierarchy

cd && mkdir apps && cd apps && git clone https://github.com/TheRinger/ImgurWallpaper.git

setup a cron job to run every 5 minutes,
crontab -e
add this line to your cron replacing USER with your username
```
*/5     *       *       *       *       /home/USER/apps/ImgurWallpaper/getImgur.py
```
