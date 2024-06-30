# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from FallenMusic import BOT_NAME

PM_START_TEXT = """
Merhaba {0}, 🥀
๏ Ben **{1}**!

➻ BotAltyapi Kanalı tarafından Türkçe şeklinde tasarlanmış bir botum.
"""

START_TEXT = """
**Merhaba** {0}, 🥀
  Şimdi **{2}** üzerinde şarkı çalabilirim.

──────────────────
➻ Benim hakkımda yardım almak veya bir şey sormak istersen [destek sohbetine katılabilirsin]({3}).
"""

HELP_TEXT = f"""
<u>❄ **{BOT_NAME} KULLANICILARI İÇİN KULLANILABİLİR KOMUTLAR :**</u>

๏ /oynat : Video sohbetinde istenen parçayı çalmaya başlar.
๏ /durdur : Şu anda çalan akışı duraklatır.
๏ /devam : Duraklatılmış akışı devam ettirir.
๏ /atla : Şu anda çalınan akışı atlar ve sıradaki parçayı çalmaya başlar.
๏ /son : Sırayı temizler ve şu anda çalınan akışı sonlandırır.

๏ /ping : Botun ping'ini ve sistem istatistiklerini gösterir.
๏ /sudolist : Botun sudo kullanıcılarının listesini gösterir.

๏ /indir : İstenen şarkıyı indirir ve size gönderir.

๏ /arama : Verilen sorguyu YouTube'da arar ve sonuçları size gösterir.
"""

HELP_SUDO = f"""
<u>✨ **{BOT_NAME} SUDO KOMUTLARI :**</u>

๏ /activevc : Şu anda aktif olan sesli sohbetlerin listesini gösterir.
๏ /eval or /sh : Verilen kodu botun terminalinde çalıştırır.
๏ /speedtest : Botun sunucusunda bir hız testi yapar.
๏ /sysstats : Botun sunucu sistem istatistiklerini gösterir.

๏ /setname [metin veya yanıt olarak metin] : Asistan hesap adını değiştirir.
๏ /setbio [metin veya yanıt olarak metin] : Asistan hesap biyografisini değiştirir.
๏ /setpfp [yanıt olarak fotoğrafa] : Asistan hesap profil fotoğrafını değiştirir.
๏ /delpfp : Asistan hesap profil fotoğrafını siler.
"""

HELP_DEV = f"""
<u>✨ **{BOT_NAME} SAHİBİ KOMUTLARI :**</u>

๏ /config : Botun tüm yapılandırma değişkenlerini almak için.
๏ /broadcast [mesaj veya bir mesaja cevap] : Mesajı botun sunucu sohbetlerine yayınlar.
๏ /rmdownloads : Botun sunucu üzerinde indirilen önbellek dosyalarını temizler.
๏ /leaveall : Asistan hesabının tüm sohbetleri terk etmesini sağlar.

๏ /addsudo [kullanıcı adı veya bir kullanıcıya cevap] : Kullanıcıyı sudo kullanıcılar listesine ekler.
๏ /rmsudo [kullanıcı adı veya bir kullanıcıya cevap] : Sudo kullanıcılar listesinden kullanıcıyı kaldırır.
"""
