; F23キーが押されたときにChromeでURLを開く "CHROME1"
F23::
Run, chrome.exe "https://github.com/rivinext/macropad-keybow2040"
return

; F24キーが押されたときに複数のURLを順に開く（遅延付き） "CHROME2"
F24::
Run, chrome.exe "https://bento.me/rivi"
Sleep, 100  ;
Run, chrome.exe "https://x.com/home"
return
