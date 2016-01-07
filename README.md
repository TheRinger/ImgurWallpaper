# ImgurWallpaper
Python App that downloads random image from /r/wallpapers/new/ and replaces desktop wallpaper

to install to same directory hierarchy

cd && mkdir apps && cd apps && git clone https://github.com/TheRinger/ImgurWallpaper.git

setup a cron job to run every 5 minutes,
crontab -e
add this line without the quotes and replaceing <USER> with your username

"*/5     *       *       *       *       /home/<USER>/apps/ImgurWallpaper/getImgur.py"
