# Step 1 - Go to Deezer via a google search
# ------------------------------------------
paste(Pattern("browser_bar.png").similar(0.90), 'http://google.com')
sleep(2)
type(Key.ENTER)
sleep(2)
click(Pattern("google_search_bar.png").targetOffset(-238,2))
type('deezer')
sleep(5)
type(Key.ENTER)
sleep(3)

click(Pattern("google_deezer_result.png").similar(0.51).targetOffset(-131,-7))
wait("deezer_head.png")
sleep(3)

# Step 2 - Make a basic search and launch a sound
# -----------------------------------------------
click(Pattern("deezer_search_bar.png").similar(0.90).targetOffset(-149,2))
type('justin bieber')
sleep(5)
type('a', KeyModifier.CTRL) 
type(Key.BACKSPACE)
type('isley brothers shout')
sleep(3)
type(Key.ENTER)
sleep(3)
click(Pattern("deezer_artist_tib.png").similar(0.90).targetOffset(-30,16))
sleep(3)
click(Pattern("deezer_tib_shout.png").similar(0.90))
sleep(10)
click(Pattern("deezer_player_pause.png").similar(0.90))
sleep(3)

# Step 3 - Buy a premium access
# -----------------------------
click(Pattern("deezer_head.png").similar(0.90).targetOffset(29,-1))
sleep(3)
click(Pattern("deezer_head_offer_menu.png").similar(0.90).targetOffset(-133,-149))
sleep(5)
click(Pattern("deezer_offer_premiumplus.png").similar(0.90).targetOffset(0,256))
