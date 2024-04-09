@namespace
class SpriteKind:
    Coin = SpriteKind.create()
    Health = SpriteKind.create()
    Reward = SpriteKind.create()

def on_overlap_tile(sprite, location):
    game.over(False, effects.slash)
    music.wawawawaa.play_until_done()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    global current_level
    current_level += 1
    start_level()
    Level_Spawn_Points()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile2)

def on_a_pressed():
    global canDoubleJump
    if Hero.vy == 0:
        Hero.vy = -100
    if Hero.is_hitting_tile(CollisionDirection.BOTTOM):
        Hero.vy = -180
    elif canDoubleJump:
        Hero.vy = -100
        canDoubleJump = False
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite3, otherSprite):
    otherSprite.destroy(effects.confetti, 500)
    music.ba_ding.play()
    info.change_score_by(1)
    scene.camera_shake(2, 100)
sprites.on_overlap(SpriteKind.player, SpriteKind.Reward, on_on_overlap)

def on_overlap_tile3(sprite4, location3):
    
    def on_start_cutscene():
        global BagOpened
        story.print_dialog("A bag. Open it?", 80, 90, 50, 150)
        story.show_player_choices("Yes", "No")
        if story.check_last_answer("Yes"):
            story.print_dialog("You found a book.", 80, 90, 50, 150)
            story.print_dialog("Carpenter", 80, 90, 50, 150)
            BagOpened += 1
        else:
            story.print_dialog("Okay.", 80, 90, 50, 150)
            info.set_life(0)
        story.cancel_current_cutscene()
    story.start_cutscene(on_start_cutscene)
    
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile12
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite5, location4):
    game.over(False, effects.melt)
    music.wawawawaa.play_until_done()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava1,
    on_overlap_tile4)

def on_overlap_tile5(sprite6, location5):
    game.over(False, effects.slash)
    music.wawawawaa.play_until_done()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_water,
    on_overlap_tile5)

def start_level():
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Reward)
    if current_level == 0:
        # This will be your "platform" for level 1. Start with designing this to create your world. You can use the pre-made gallery tiles or create your own. 
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
        scene.set_background_image(img("""
            1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                        11111111111111111bbbb111111111111111111111111111111111111bbbb111111111111111111111111111111111111bbbb111111111111111111111111111111111111bbbb1111111111111111111
                        11111111111bbbbbbbbbbb11111111111111111111111111111bbbbbbbbbbb11111111111111111111111111111bbbbbbbbbbb11111111111111111111111111111bbbbbbbbbbb111111111111111111
                        11111111bbbbbbbbbbbbbb11111111111111111111111111bbbbbbbbbbbbbb11111111111111111111111111bbbbbbbbbbbbbb11111111111111111111111111bbbbbbbbbbbbbb111111111111111111
                        111111bbbbbbbbbbbbbbbb111111111111111111111111bbbbbbbbbbbbbbbb111111111111111111111111bbbbbbbbbbbbbbbb111111111111111111111111bbbbbbbbbbbbbbbb111111111111111111
                        11111bbbbbbbbbbbbbbbbb11111111111111111111111bbbbbbbbbbbbbbbbb11111111111111111111111bbbbbbbbbbbbbbbbb11111111111111111111111bbbbbbbbbbbbbbbbb111111111111111111
                        11111bbbbbbbbbbbbbbbbb11111111111111111111111bbbbbbbbbbbbbbbbb11111111111111111111111bbbbbbbbbbbbbbbbb11111111111111111111111bbbbbbbbbbbbbbbbb111111111111111111
                        1111bbbbbbbbbbbbbbbbbbb111111111111111111111bbbbbbbbbbbbbbbbbbb111111111111111111111bbbbbbbbbbbbbbbbbbb111111111111111111111bbbbbbbbbbbbbbbbbbb11111111111111111
                        1111bbbbbbbbbbbbbbbbbbb111111111111111111111bbbbbbbbbbbbbbbbbbb111111111111111111111bbbbbbbbbbbbbbbbbbb111111111111111111111bbbbbbbbbbbbbbbbbbb11111111111111111
                        111bbbbbbbbbbbbbbbbbbbb111111bbb11111111111bbbbbbbbbbbbbbbbbbbb111111bbb11111111111bbbbbbbbbbbbbbbbbbbb111111bbb11111111111bbbbbbbbbbbbbbbbbbbb111111bbb11111111
                        111bbbbbbbbbbbbbbbbbbbb11111bbbbb1111111111bbbbbbbbbbbbbbbbbbbb11111bbbbb1111111111bbbbbbbbbbbbbbbbbbbb11111bbbbb1111111111bbbbbbbbbbbbbbbbbbbb11111bbbbb1111111
                        11bbbbbbbbbbbbbbbbbbbbb11111bbbbb111111111bbbbbbbbbbbbbbbbbbbbb11111bbbbb111111111bbbbbbbbbbbbbbbbbbbbb11111bbbbb111111111bbbbbbbbbbbbbbbbbbbbb11111bbbbb1111111
                        11bbbbbbbbbbbbbbbbbbbbb11111bbbbb111111111bbbbbbbbbbbbbbbbbbbbb11111bbbbb111111111bbbbbbbbbbbbbbbbbbbbb11111bbbbb111111111bbbbbbbbbbbbbbbbbbbbb11111bbbbb1111111
                        11bbbbbbbbbbbbbbbbbbbbb11111bbbbbb11111111bbbbbbbbbbbbbbbbbbbbb11111bbbbbb11111111bbbbbbbbbbbbbbbbbbbbb11111bbbbbb11111111bbbbbbbbbbbbbbbbbbbbb11111bbbbbb111111
                        1bbbbbbbbbbbbbbbbbbbbbb11111bbbbbb1111111bbbbbbbbbbbbbbbbbbbbbb11111bbbbbb1111111bbbbbbbbbbbbbbbbbbbbbb11111bbbbbb1111111bbbbbbbbbbbbbbbbbbbbbb11111bbbbbb111111
                        1bbbbbbbbbbbbbbbbbbbbbb11111bbbbbb1111111bbbbbbbbbbbbbbbbbbbbbb11111bbbbbb1111111bbbbbbbbbbbbbbbbbbbbbb11111bbbbbb1111111bbbbbbbbbbbbbbbbbbbbbb11111bbbbbb111111
                        1bbbbbbbbbbbbbbbbbbbbbb1111bbbbbbb1111111bbbbbbbbbbbbbbbbbbbbbb1111bbbbbbb1111111bbbbbbbbbbbbbbbbbbbbbb1111bbbbbbb1111111bbbbbbbbbbbbbbbbbbbbbb1111bbbbbbb111111
                        bbbbbbbbbbbbbbbdbbbbbbb1111bbbbbbb1111bbbbbbbbbbbbbbbbbdbbbbbbb1111bbbbbbb1111bbbbbbbbbbbbbbbbbdbbbbbbb1111bbbbbbb1111bbbbbbbbbbbbbbbbbdbbbbbbb1111bbbbbbb1111bb
                        bbbbbbbbbbbbbbddbbbbbbb1111bbbbbbb11bbbbbbbbbbbbbbbbbbddbbbbbbb1111bbbbbbb11bbbbbbbbbbbbbbbbbbddbbbbbbb1111bbbbbbb11bbbbbbbbbbbbbbbbbbddbbbbbbb1111bbbbbbb11bbbb
                        bbbbbbbbbbbbbbddbbbbbbb1111bbbbbbbb1bbbbbbbbbbbbbbbbbbddbbbbbbb1111bbbbbbbb1bbbbbbbbbbbbbbbbbbddbbbbbbb1111bbbbbbbb1bbbbbbbbbbbbbbbbbbddbbbbbbb1111bbbbbbbb1bbbb
                        bbbbbbbbbbbbbddddbbbbbb1111bbbbbbbbbbbbbbbbbbbbbbbbbbddddbbbbbb1111bbbbbbbbbbbbbbbbbbbbbbbbbbddddbbbbbb1111bbbbbbbbbbbbbbbbbbbbbbbbbbddddbbbbbb1111bbbbbbbbbbbbb
                        bbbbbbbbbbbdddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbdddbbbbbbbbbbbbbbbeeeeeeebbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbeeeeeeebbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbeeeeeeebbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbeeeeeeebb
                        bbbbbbbbbbbbdddddbbbbbbbbbbbbeeeeeeeeeeebbbbbbbbbbbbdddddbbbbbbbbbbbbeeeeeeeeeeebbbbbbbbbbbbdddddbbbbbbbbbbbbeeeeeeeeeeebbbbbbbbbbbbdddddbbbbbbbbbbbbeeeeeeeeeee
                        bbbbbbbbbbbbdddddddbbbbbbbbbeeeeeeeeeeeeebbbbbbbbbbbdddddddbbbbbbbbbeeeeeeeeeeeeebbbbbbbbbbbdddddddbbbbbbbbbeeeeeeeeeeeeebbbbbbbbbbbdddddddbbbbbbbbbeeeeeeeeeeee
                        bbbbbbbbbbbddddddbbbbbbbbbeeeeeeeeeeeeeeeeebbbbbbbbddddddbbbbbbbbbeeeeeeeeeeeeeeeeebbbbbbbbddddddbbbbbbbbbeeeeeeeeeeeeeeeeebbbbbbbbddddddbbbbbbbbbeeeeeeeeeeeeee
                        bbbbbbbbbdddddddddbbbbbbbeeeeeeeeeeeeeeeeeeebbbbbdddddddddbbbbbbbeeeeeeeeeeeeeeeeeeebbbbbdddddddddbbbbbbbeeeeeeeeeeeeeeeeeeebbbbbdddddddddbbbbbbbeeeeeeeeeeeeeee
                        bbbbbbbbbbbddddddddbbbbbeeeeeeeeeeeeeeeeeeeeebbbbbbddddddddbbbbbeeeeeeeeeeeeeeeeeeeeebbbbbbddddddddbbbbbeeeeeeeeeeeeeeeeeeeeebbbbbbddddddddbbbbbeeeeeeeeeeeeeeee
                        bbbbbbbbbbdddddddbbbbbbeeeeeeeeeeeeeeeeeeeeeeebbeedddddddbbbbbbeeeeeeeeeeeeeeeeeeeeeeebbeedddddddbbbbbbeeeeeeeeeeeeeeeeeeeeeeebbeedddddddbbbbbbeeeeeeeeeeeeeeeee
                        bbbbbbbbbbbbddddddbbbbeedeeeeeeeeeeeeeeeeeeeeeeeeeeeddddddbbbbeedeeeeeeeeeeeeeeeeeeeeeeeeeeeddddddbbbbeedeeeeeeeeeeeeeeeeeeeeeeeeeeeddddddbbbbeedeeeeeeeeeeeeeee
                        bbbbbbbbbbdddddddddbbeeedeeeeeeeeeeeeeeeeeeeeeeeeedddddddddbbeeedeeeeeeeeeeeeeeeeeeeeeeeeedddddddddbbeeedeeeeeeeeeeeeeeeeeeeeeeeeedddddddddbbeeedeeeeeeeeeeeeeee
                        bbbbbbbbbdddddddddddeeeddeeeeeeeeeeeeeeeeeeeeeeeedddddddddddeeeddeeeeeeeeeeeeeeeeeeeeeeeedddddddddddeeeddeeeeeeeeeeeeeeeeeeeeeeeedddddddddddeeeddeeeeeeeeeeeeeee
                        bbbbbbbdddddddddddeeeeeeddeeeeeeeeeeeeeeeeeeeeedddddddddddeeeeeeddeeeeeeeeeeeeeeeeeeeeedddddddddddeeeeeeddeeeeeeeeeeeeeeeeeeeeeddddddddddddddeeeddeeeeeeeeeeeeee
                        bbbbbbbdbdddddddddeeeeeddeeeeeeeeeeeeeeeeeeeeeeeedddddddddeeeeeddeeeeeeeeeeeeeeeeeeeeeeeedddddddddeeeeeddeeeeeeeeeeeeeeeeeeeeeeeedddddddddddeeeddeeeeeeeeeeeeeee
                        bbbbbbbdbdddddddeeeeeeddddeeeeeeeeeeeeeeeeeeeeeeedddddddeeeeeeddddeeeeeeeeeeeeeeeeeeeeeeedddddddeeeeeeddddeeeeeeeeeeeeeeeeeeeeeeedddddddddeeeeddddeeeeeeeeeeeeee
                        bbbbbbbddddddddddddeeddddddeeeeeeeeeeeeeeeeeeeeedddddddddddeeddddddeeeeeeeeeeeeeeeeeeeeedddddddddddeeddddddeeeeeeeeeeeeeeeeeeeeedddddddddddeeddddddeeeeeeeeeeeee
                        bbbbbbbbdbddddddddddeeeddeeeeeeeeeeedeeeeeeeeeeeeeddddddddddeeeddeeeeeeeeeeedeeeeeeeeeedddddddddddddeeeddeeeeeeeeeeedeeeeeeeeeeeeeddddddddddeeeddeeeeeeeeeeedeee
                        bbbbbbbbdddddddddddeeddddddeeeeeeeeedeeeeeeeeeeedddddddddddeeddddddeeeeeeeeedeeeeeeeeeeedddddddddddeeddddddeeeeeeeeedeeeeeeeeeeedddddddddddeeddddddeeeeeeeeedeee
                        bbbdbbbddddddddddddeddddddddeeeeeeedddeeeeedeeeddddddddddddeddddddddeeeeeeedddeeeeedeeeddddddddddddeddddddddeeeeeeedddeeeeedeeeddddddddddddeddddddddeeeeeeedddee
                        bbbddbbbbbddddddddddddddddeeeeeeeeeeddeeeeeddeeeeeddddddddddddddddeeeeeeeeeeddeeeeeddeeeeeddddddddddddddddeeeeeeeeeeddeeeeeddeeeddddddddddddddddddeeeeeeeeeeddee
                        bbddbbbbddddddddddddddddddddeeeeeeeddeeeeeddeeeeddddddddddddddddddddeeeeeeeddeeeeeddeeeeddddddddddddddddddddeeeeeeeddeeeeeddeeeeddddddddddddddddddddeeeeeeeddeee
                        bbbddbbddddddddddddddddddddddeeeeeddddeeeeeddeeddddddddddddddddddddddeeeeeddddeeeeeddeeddddddddddddddddddddddeeeeeddddeeeeeddeeddddddddddddddddddddddeeeeeddddee
                        bbdddddddddddddddddddddddddeeeeeeeeddddeeedddddddddddddddddddddddddeeeeeeeeddddeeedddddddddddddddddddddddddeeeeeeeeddddeeedddddddddddddddddddddddddeeeeeeeedddde
                        bbbddddddddddddddddddddddddddeeeeeddddeeeeeddddddddddddddddddddddddddeeeeeddddeeeeeddddddddddddddddddddddddddeeeeeddddeeeeeddddddddddddddddddddddddddeeeeeddddee
                        bbbdddddddddddddddddddddddddddeeeddddddeeeedddddddddddddddddddddddddddeeeddddddeeeedddddddddddddddddddddddddddeeeddddddeeeedddddddddddddddddddddddddddeeedddddde
                        bbddddddddddddddddddddddddddeeeeeeddddeeeeddddddddddddddddddddddddddeeeeeeddddeeeeddddddddddddddddddddddddddeeeeeeddddeeeeddddddddddddddddddddddddddeeeeeeddddee
                        bdddddddddddddddddddddddddddddeedddddddeedddddddddddddddddddddddddddddeedddddddeedddddddddddddddddddddddddddddeedddddddeedddddddddddddddddddddddddddddeeddddddde
                        bbdddddddddddddddddddddddddddddeedddddddeedddddddddddddddddddddddddddddeedddddddeedddddddddddddddddddddddddddddeedddddddeedddddddddddddddddddddddddddddeeddddddd
                        bbddddddddddddddddddddddddddddeeddddddddeeddddddddddddddddddddddddddddeeddddddddeeddddddddddddddddddddddddddddeeddddddddeeddddddddddddddddddddddddddddeedddddddd
                        dddddddddddddddddddddddddddddddedddddddddddddddddddddddddddddddddddddddedddddddddddddddddddddddddddddddddddddddedddddddddddddddddddddddddddddddddddddddedddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        """))
    elif current_level == 1:
        tiles.set_current_tilemap(tilemap("""
            level5
        """))
    elif current_level == 2:
        tiles.set_current_tilemap(tilemap("""
            level18
        """))
    elif current_level == 3:
        game.game_over(True)

def on_life_zero():
    game.over(False, effects.melt)
info.on_life_zero(on_life_zero)

def Starting_Game_Mechanics():
    global Hero, canDoubleJump
    Hero = sprites.create(assets.image("""
        myImage0
    """), SpriteKind.player)
    scene.camera_follow_sprite(Hero)
    controller.move_sprite(Hero, 100, 0)
    Hero.ay = 200
    canDoubleJump = True
    info.set_score(0)
    info.set_life(3)
def Level_Spawn_Points():
    global Reward2, BadGuy1
    # This is a spawn point on the tilemap for the hero. This tile will be replaced by the hero sprite
    for value in tiles.get_tiles_by_type(assets.tile("""
        Hero Spawn Point
    """)):
        tiles.place_on_tile(Hero, value)
        tiles.set_tile_at(value, assets.tile("""
            transparency16
        """))
    # This is a spawn point for rewards. This tile will be replaced by your reward sprite. The art should be replaced with yours.
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        Reward Spawn
    """)):
        Reward2 = sprites.create(img("""
                ffffffffffffffffffffffffffffffff
                            f336666333666333366663666663333f
                            f336336333666633363663636363333f
                            f336663336666633363633663663333f
                            f333333333333333366633333333333f
                            f333333333333333336333333333333f
                            f333333333333333333333333333333f
                            f333373333333333333333333333333f
                            f337777737733777377737773733733f
                            f337373333733737373737373737333f
                            f337777733733737373737373773333f
                            f333373733733737373737373737333f
                            f337777737773777377737773733733f
                            f333373333333333333333333333333f
                            f333333333333333333333333333333f
                            ffffffffffffffffffffffffffffffff
            """),
            SpriteKind.Reward)
        tiles.place_on_tile(Reward2, value2)
        tiles.set_tile_at(value2, assets.tile("""
            transparency16
        """))
    # This is a spawn point for rewards. This tile will be replaced by your reward sprite. The art should be replaced with yours.
    for value3 in tiles.get_tiles_by_type(assets.tile("""
        Enemy Spawn Points
    """)):
        BadGuy1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . 2 2 . . . . . 2 2 . . . . 
                            . . . 2 2 . . . . . 2 2 . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 2 2 2 2 2 2 2 2 . . . 
                            . . . . 2 2 . . . . . . 2 2 . . 
                            . . . 2 2 . . . . . . . . 2 . . 
                            . . . 2 . . . . . . . . . 2 2 . 
                            . . 2 . . . . . . . . . . . 2 . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.enemy)
        tiles.place_on_tile(BadGuy1, value3)
        tiles.set_tile_at(value3, assets.tile("""
            transparency16
        """))

def on_overlap_tile6(sprite7, location6):
    game.over(True, effects.confetti)
    music.power_up.play()
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_open,
    on_overlap_tile6)

def on_on_overlap2(sprite8, otherSprite2):
    otherSprite2.destroy(effects.ashes, 100)
    scene.camera_shake(2, 200)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

BadGuy1: Sprite = None
Reward2: Sprite = None
BagOpened = 0
canDoubleJump = False
Hero: Sprite = None
current_level = 0
Starting_Game_Mechanics()
current_level = 0
start_level()
Level_Spawn_Points()

def on_on_update():
    global canDoubleJump
    if Hero.is_hitting_tile(CollisionDirection.BOTTOM):
        canDoubleJump = True
game.on_update(on_on_update)
