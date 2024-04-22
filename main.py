@namespace
class SpriteKind:
    Coin = SpriteKind.create()
    Health = SpriteKind.create()
    Reward = SpriteKind.create()
    Resource = SpriteKind.create()
    SpectatorSprite = SpriteKind.create()
    EnemyProjectile = SpriteKind.create()

def on_overlap_tile(sprite, location):
    Damage()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_on_overlap(sprite8, otherSprite2):
    otherSprite2.destroy(effects.ashes, 100)
    Damage()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_b_pressed():
    global Spectate
    if Spectate == 1:
        Spectate += -1
        ExitSpectate()
    elif ShieldStatus == 1:
        BKeyPressed(True)
    else:
        BKeyPressed(False)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def Level_Spawn_Points():
    global Reward2, Resource2, myEnemy
    sprites.destroy_all_sprites_of_kind(SpriteKind.Resource)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Reward)
    sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
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
                            f336666636666633666663666663333f
                            f336333636333633633363633363333f
                            f336666636666633666663666663333f
                            f333333333333333333333333333333f
                            f333333333333333333333333333333f
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
    for value22 in tiles.get_tiles_by_type(assets.tile("""
        myTile8
    """)):
        Resource2 = sprites.create(assets.image("""
            myImage
        """), SpriteKind.Resource)
        tiles.place_on_tile(Resource2, value22)
        tiles.set_tile_at(value22, assets.tile("""
            transparency16
        """))
    # This is a spawn point for rewards. This tile will be replaced by your reward sprite. The art should be replaced with yours.
    for value222 in tiles.get_tiles_by_type(assets.tile("""
        Enemy Spawn Points
    """)):
        myEnemy = sprites.create(assets.image("""
            Enemy1
        """), SpriteKind.enemy)
        tiles.place_on_tile(myEnemy, value222)
        tiles.set_tile_at(value222, assets.tile("""
            transparency16
        """))
        myEnemy.follow(Hero, 50)
        myEnemy.ay = 500
def Starting_Game_Mechanics():
    global ResourceAmount, Hero, canDoubleJump
    scene.set_background_image(img("""
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333666633333333333333333333333333333333333333333333333333333333333333333333333333333366663333333333333333333333333333333333333333333333333333
                3333333333333333333336666663333333333333333333333333333333333333333333333333333333333333333333333333333666666333333333333333333333333333333333333333333333333333
                3333333333333333333336666663366333333333333333333333333333333333333333333333333333333333333333333333333666666336633333333333333333333333333333333333333333333333
                3333333333333333336666666663666663333333333333333333333333333333333333333333333333333333333333333333666666666366666333333333333333333333333333333333333333333333
                3333333333333333366666666666666663333333333333333333333333333333333333333333333333333333333333333336666666666666666333333333333333333333333333333333333333333333
                3333333333333333666666666666666666633333333333333333333333333333333333333333333333333333333333333366666666666666666663333333333333333333333333333333333333333333
                3333333333333333666666666666666666663333333333333333333333333333333333333333333333333333333333333366666666666666666666333333333333333333333333333333333333333333
                3333333333333333366666666666666666663336633333333333333333333333333333333333333333333333333333333336666666666666666666333663333333333333333333333333333333333333
                3333333333333666636666666666666666663366666333333333333333333333333333333333333333333333333333366663666666666666666666336666633333333333333333333333333333333333
                3333333333336666663666666666666666633366666333333333333333333333333333333333333333333333333333666663366666666666666663336666633333333333333333333333333333333333
                3333333333336666663666666666666666366666666633333333333333333333333333333333333333333333333333666666666666666666666636666666663333333333333333333333333333333333
                3333333333336666666666666666666666666666666633333333333333333333333333333333333333333333333333666666666666666666666666666666663333333333333333333333333333333333
                3333333333333666666666666666666666666666666633333333333333333333333333333333333333333333333333366666666666666666666666666666663333333333333333333333333333333333
                3366633336666366666666666666666666666666666336633333333333336666333333333333333333336663333666636666666666666666666666666666633663333333333333666633333333333333
                3666663366666666666666666666666666666666666366663333333333366666633333333333333333366666336666636666666666666666666666666666636666333333333336666663333333333333
                3666663666666666666666666666666666666666666366663333333333366666636663333333333333366666366666666666666666666666666666666666636666333333333336666663666333333333
                3366666666666666666666666666666666666666666666663333333333333666666666333333333333336666666666666666666666666666666666666666666666333333333333366666666633333333
                3666666666666666666666666666666666666666666666633333333366663666666666333333333333366666666666666666666666666666666666666666666663333333336666366666666633333333
                6666666666666666666666666666666666666666666666663333333666666666666663333333333133666666666aa6666666666666666666666666666666666666333333366666666666666333333333
                6666666666666666666666666666666666666666666666666366633666666666666666666333333aaa666666666aaa666666666666666666666666666666666666636663366666666666666666633333
                6666666666666666666666666666666666666666666666666666666666666666666666666633331aaa666666666aaa666666666666666666666666666666666666666666666666666666666666663333
                66666666666666666666666666666666666666666666666666666666666666666666666666333aaaaaaa666666aaaaa66666666666666666666666666666666666666666666666666666666666663333
                66666666666666666666666666666666666666666aaaaaaaaa666666666666666666666666666aaaaaaa666666aaaaa666666666666666666666666666666666666666666aaaaaaaaaa6666666666666
                66666666666666666666666666666666666666666aaaaaaaaa666666666666666666666666666aaaaaaa666666aaaaa666666666666666666666666666666666666666666aaaaaaaaaa6666666666666
                6666666666666666666aaa6666666666666666666a11aaaaaa666666666666666666666666666a11aaaa66666aaaaaaa66666666666666666666aa6666666666666666666aa1a1aaaaa6666666666666
                666666666666666666aaaaa666666666666666666aaaaaaa1a666666666666666666666666666aaaaaaa66666aaaaaaa6666666666666666666aaaa666666666666666666aaaaaa11aa6666666666666
                66666666666666666aaaaaa666666666666666666aaaaaaaaa6666666666a66666666aaaaa666a1aaaaa66666aaaaaaa66666666666666666aaaaaa666666666666666666aaaaaaaaaa6666666666666
                66666666666666666aaa1a666666a666666666666aaaaaaaaa666666666aa66666666aaaaa666aaaaaaa66666aaaaaaa66666666666666666aaa1a666666aa66666666666aaaa1aaaaa66666666aa666
                66666666666666666aaaaaa66666a666666666666aaaaaaa1a666666666aa66666666aaaaa666aaaaaaa66666aaaaaaa66666666666666666aaaaaa66666aa66666666666aaaaaaa1aa66666666aa666
                66666666aaa666666aa11a66666aaa66666666666aaaaaaaaa66aaaaaa6aa63666666aaaaa666aaaaaaa66666aaaaaaa666666666aa666666aaa1a66666aaa66666666666aaaaaaaaaa6aaaaaaaaa666
                a6aa6666aaaaaaaaaaa1aaa666aaaaa6666666666aaaaaaa1a66a11aaa6aa666666666aa1aa66aaaaaaa666aaaaaaaaaa6aa6666aaaaaaaaaaaaa1a6666aaaa6666666666aaaaaa11aa6a11aaaaaa666
                aaaa66666a1aa1aaaaaaaaa666aaaaa6666666666aaaaaaaaa66aaaa1a6aa66666666aaaaaa66aa1aaaa666aaaaaaaaaaaaa6666aa1aaa1aaaaaaaa6666aaaa6666666666aaaaaaaaaa6aaaa1aaaa666
                aa1a66666aaa1111aaaaaaa666aaaaa6666666666aaaaaaaaa66aaaa1aaaa66666666aaaaaa66aaaaaaa666aaaaaaaaaaa1a6666aaaa1a11aaaaaaa6666aaaa6666666666aaaaaaaaaa6aaaa1aaaa666
                aaaa6666aaaaaaaaaaaaaaaa66aaaaaa66aa6aa6aaaaaaaaaaa6a11aaaaaa66666666aaaaaa66aaaaaaa666aaaaaaaaaaaaa6666aaaaaaaaaaaaaaaa66aaaaaa666a66aaaaaaaaaaaaa6a11aaaaaa666
                aa1a6666aaaaaaaaaaaaaaaa66aaaaaa66aaaaaaaaaaaaaaaaa6aaaaaaaaa66a66a66aaaaaa66aaaaaaa666aaaaaaaaaaa1a6666aaaaaaaaaaaaaaaa66aaaaaa666aaaaaaaaaaaaaaaa6aaaaaaaaa666
                aaaaa6aa1a1aaaaaaaaaaaaa66aaaaaaa6aaaa11aaaaaaaaaaaaa11ccaaaaaaa6aaa66aa1aa66aaaaaaa666aaaaaaaaaaaaaaa6aaa1aaaaaaaaaaaaa66aaaaaaa666a11aaaaaacaaaaaaa11cccaaa6aa
                aaaaa6aaaaaaaaaaaaaaaaaaaa1aaaaaa6aaaaaaaaacccaaaaaaaaacccaaaaaa6aaa6aaaaaa66aaaaaaa666aaaaaaaaaaaaaaa6aaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaaaaaccaaaaaaaaacccaaa6aa
                aaaaa6aaaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaaaacccaaaaaaaaacccaaaaaaaaaaaaaaaaaaaaaaaaaa666aaaaaaaaaaaaaaa6aaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaaaaaccaaaaaaaaacccaaaaaa
                aaaaa6aaaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaacccccccaaaaaacccccaaaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaaaaaaaaaa6aaaaaaaaaaaaaaaaaaaaaaaaaa6a1aaaaaacccccccaaaaacccccaaaaa
                aaaaacccccccccaaaaaaaaaaaaaaaaaaa6aaaaaaacccccccaaaaaacccccaaaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaaaaaaaaaccccccccccaaaaaaaaaaaaaaaaaa6aaaaaaaacccccccaaaaacccccaaaaa
                aaaaacccccccccaaaaaaaaaaaaaaaaaaa6aaaaaaacccccccaaaaaacccccaaaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaaaaaaaaaccccccccccaaaaaaaaaaaaaaaaaa6aaaaaaaacccccccaaaaacccccaaaaa
                aaaaacddccccccaaaaaaaaaaaaaaaaaaa6aaaaaaacddccccaaaaacccccccaa111aaaaaaaaaaaaaaaccaaaa6aaaaaaaaaaaaaaccdcdcccccaaaaaaaaaaaaaaaaaa6aaaaaaaacccccccaaaacccccccc11a
                aaaaacccccccdcaaaaaaaaaaaaaaaaaaa6aaaaaaacccccccaaaaacccccccaaa11aaaaaaaaaaaaaaccccaaa6aaaaaaaaaaaaaaccccccddccaaaaaaaaaaaaaaaaaa6aaaaaaaacccccccaaaaccccccccaaa
                aaaaacccccccccaaaaaaaaaacaaaaaaaacccccaaacdcccccaaaaacccccccaaaaaaaaaaa1aaaaaccccccaaa6aaaaaaaaaaaaaaccccccccccaaaaaaaaaaaaaaaaaaaccccaaaacccdcccaaaaccccccccaaa
                aaaaacccccccccaaaaaaaaaccaaaaaaaacccccaaacccccccaaaaacccccccaa1aaaaaaaaaaaaaacccdcaaaaaaccaaaaaaaaaaaccccdcccccaaaaaaaaccaaaaaaaaaccccaaaacccdcccaaaacccccccca1a
                aaaaacccccccdcaaaaaaaaaccaaaaaaaacccccaaacccccccaaaaacccccccaa111aaaaaaaaaaaaccccccaaaaaccaaaaaaaaaaacccccccdccaaaaaaaaccaaaaaaaaccccccaaacccccccaaaacccccccc11a
                aaaaacccccccccaaccccccaccaaaaaaaacccccaaacccccccaaaaacccccccaaaaaaaaacc1aaaaacccdcaaaaacccaaaaaaaaaaaccccccccccacccccccccaaaaaaaaccccccaaacccdcccaaaaccccccccaaa
                aaaaacccccccdcaacddcccaccaaaaaaaaaccdccaacccccccaaaccccccccccaccaaaacccccccccccccdcaaaaccccaaaaaaaaaaccccccddccacddccccccaaaaaaaacccccccaacccccccaaccccccccccccc
                aaaaacccccccccaaccccdcaccaaaaaaaaccccccaaccdccccaaacccccccccccccaaaaccdcccdccccccccaaaaccccaaaaaaaaaaccccccccccaccccdccccaaaaaaaacccccccaaccccdccaaccccccccccccc
                aaaaacccccccccaaccccdccccaaaaaaaaccccccaacccccccaaacccccccccccdcaaaaccccdcddcccccccaaaaccccaaaaaaaaaaccccccccccaccccdccccaaaaaaaacccccccaacccccccaaccccccccccccc
                accacccccccccccacddccccccaaaaaaaaccccccaacccccccaaacccccccccccccaaaaccccccccccccccccaaccccccaaacaacccccccccccccacddccccccaaaaaaaacccccccaacccccccaaccccccccccccc
                cccccccccccccccacccccccccaacaacaaccccccaacccccccaaacccccccccccdcaaaaccccccccccccccccaaccccccaaaccccccccccccccccacccccccccaaaaacaacccccccaacccccccaaccccccccccccc
                ccddcccccccccccccddddcccccccacccaaccdccaacccccccaaacccccccccccccccacccdcccccccccccccaacccccccaaacddccccccccccccccddcdccccaccacccacccccccaacccccccaaccccccccccccc
                ccccccccccccccccccccccccccccacccaccccccaacccccccaaacccccccccccccccaccccccccccccccccccccccccccacccccccccccccccccccccccccccaccacccccccccccaaccccdccaaccccccccccccc
                ccccccccccccccccccccccccccccccccccccccccccccccccaaacccccccccccccccaccccccccccccccccccccccccccacccccccccccccccccccccccccccccccccccccccccccccccccccaaccccccccccccc
                ccccccccccccccccccccccccccccccccccccccccccccccccccacccccccccccccccaccccccccccccccccccccccccccacdccccccccccccccccccccccccccccccccccccccccccccccccccaccccccccccccc
                ccccccccccccccccccccccccccccccccccccccccccccccccccacccccccccccccccaccccccccccccccccccccccccccaccccccccccccccccccccccccccccccccdcccccccccccccccccccaccccccccccccc
                ccccccccccccccccccccccccccccccccccccccccccccccccccacccccccccccccccaccccccccccccccccccccccccccaccccccccccccccccccccccccccccccccccccccccccccccccccccaccccccccccccc
                ccccccccccccccccccccccccccdddcccccccccccccccccccccacccccccccccccccaccccccccccccccccccccccccccacccccccccccccccccccccccccccddcdcdccccccccccccccccccccccccccccccccc
                cccccccccccccccccccccccccccddcccccccccccccccccccccacccccccccccccccaccccccccccccccccccccccccccaccccccccccccccccccccccccccccccdcdccccccccccccccccccccccccccccccccc
                cccccccccccccccccccccccccccccccccccdccccccccccccccacccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccdccccdcccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccdcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccdccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccdddccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccddcdccccccccccccccccccccccccccccccccccc
                cccccccccccccccccccccccccccccccccccdcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
                cccccccccccccccccdccccccccccccccccdccccccccccccccccccccccdccccccccccccccccdccccccccccccccccccccccdccccccccccccccccdccccccccccccccccccccccdccccccccccccccccdccccc
                ccccccdcccddcccccddccccdcccdccccdcddcccdccccccdcccddcccccddccccdcccdccccdcddcccdccccccdcccddcccccddccccdcccdccccdcddcccdccccccdcccddcccccddccccdcccdccccdcddcccd
                ccdcccddcddccdcccddcccddcccddcccdccddcddccdcccddcddccdcccddcccddcccddcccdccddcddccdcccddcddccdcccddcccddcccddcccdccddcddccdcccddcddccdcccddcccddcccddcccdccddcdd
                ccddccddcddccddcccddcddccccddcdcddcddddcccddccddcddccddcccddcddccccddcdcddcddddcccddccddcddccddcccddcddccccddcdcddcddddcccddccddcddccddcccddcddccccddcdcddcddddb
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
    ResourceAmount = 0
    Hero = sprites.create(assets.image("""
        myImage0
    """), SpriteKind.player)
    scene.camera_follow_sprite(Hero)
    controller.move_sprite(Hero, 100, 0)
    canDoubleJump = True
    Hero.ay = 200

def on_a_pressed():
    global i, canDoubleJump
    if i < 4:
        i += 1
    else:
        i = 0
    if ShieldStatus == 1:
        if Hero.vy == 0:
            Hero.vy = -80
        if Hero.is_hitting_tile(CollisionDirection.BOTTOM):
            Hero.vy = -80
        elif canDoubleJump:
            Hero.vy = -40
            canDoubleJump = False
    elif Hero.vy == 0:
        Hero.vy = -80
    if Hero.is_hitting_tile(CollisionDirection.BOTTOM):
        Hero.vy = -120
    elif canDoubleJump:
        Hero.vy = -100
        canDoubleJump = False
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def RefreshStatus():
    global AngleShield
    if controller.right.is_pressed():
        AngleShield = 10
        if ShieldStatus == 1:
            Hero.set_image(assets.image("""
                myImage2
            """))
        else:
            Hero.set_image(assets.image("""
                myImage3
            """))
    elif controller.left.is_pressed():
        AngleShield = 170
        if ShieldStatus == 1:
            Hero.set_image(assets.image("""
                myImage8
            """))
        else:
            Hero.set_image(assets.image("""
                myImage0
            """))
def ExitSpectate():
    
    def on_start_cutscene():
        story.print_dialog("Exiting Spectate", 80, 90, 50, 150)
        story.cancel_current_cutscene()
    story.start_cutscene(on_start_cutscene)
    
    sprites.destroy_all_sprites_of_kind(SpriteKind.SpectatorSprite)
    Starting_Game_Mechanics()
    start_level()
    Level_Spawn_Points()
    scene.set_background_image(img("""
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333666633333333333333333333333333333333333333333333333333333333333333333333333333333366663333333333333333333333333333333333333333333333333333
                3333333333333333333336666663333333333333333333333333333333333333333333333333333333333333333333333333333666666333333333333333333333333333333333333333333333333333
                3333333333333333333336666663366333333333333333333333333333333333333333333333333333333333333333333333333666666336633333333333333333333333333333333333333333333333
                3333333333333333336666666663666663333333333333333333333333333333333333333333333333333333333333333333666666666366666333333333333333333333333333333333333333333333
                3333333333333333366666666666666663333333333333333333333333333333333333333333333333333333333333333336666666666666666333333333333333333333333333333333333333333333
                3333333333333333666666666666666666633333333333333333333333333333333333333333333333333333333333333366666666666666666663333333333333333333333333333333333333333333
                3333333333333333666666666666666666663333333333333333333333333333333333333333333333333333333333333366666666666666666666333333333333333333333333333333333333333333
                3333333333333333366666666666666666663336633333333333333333333333333333333333333333333333333333333336666666666666666666333663333333333333333333333333333333333333
                3333333333333666636666666666666666663366666333333333333333333333333333333333333333333333333333366663666666666666666666336666633333333333333333333333333333333333
                3333333333336666663666666666666666633366666333333333333333333333333333333333333333333333333333666663366666666666666663336666633333333333333333333333333333333333
                3333333333336666663666666666666666366666666633333333333333333333333333333333333333333333333333666666666666666666666636666666663333333333333333333333333333333333
                3333333333336666666666666666666666666666666633333333333333333333333333333333333333333333333333666666666666666666666666666666663333333333333333333333333333333333
                3333333333333666666666666666666666666666666633333333333333333333333333333333333333333333333333366666666666666666666666666666663333333333333333333333333333333333
                3366633336666366666666666666666666666666666336633333333333336666333333333333333333336663333666636666666666666666666666666666633663333333333333666633333333333333
                3666663366666666666666666666666666666666666366663333333333366666633333333333333333366666336666636666666666666666666666666666636666333333333336666663333333333333
                3666663666666666666666666666666666666666666366663333333333366666636663333333333333366666366666666666666666666666666666666666636666333333333336666663666333333333
                3366666666666666666666666666666666666666666666663333333333333666666666333333333333336666666666666666666666666666666666666666666666333333333333366666666633333333
                3666666666666666666666666666666666666666666666633333333366663666666666333333333333366666666666666666666666666666666666666666666663333333336666366666666633333333
                6666666666666666666666666666666666666666666666663333333666666666666663333333333133666666666aa6666666666666666666666666666666666666333333366666666666666333333333
                6666666666666666666666666666666666666666666666666366633666666666666666666333333aaa666666666aaa666666666666666666666666666666666666636663366666666666666666633333
                6666666666666666666666666666666666666666666666666666666666666666666666666633331aaa666666666aaa666666666666666666666666666666666666666666666666666666666666663333
                66666666666666666666666666666666666666666666666666666666666666666666666666333aaaaaaa666666aaaaa66666666666666666666666666666666666666666666666666666666666663333
                66666666666666666666666666666666666666666aaaaaaaaa666666666666666666666666666aaaaaaa666666aaaaa666666666666666666666666666666666666666666aaaaaaaaaa6666666666666
                66666666666666666666666666666666666666666aaaaaaaaa666666666666666666666666666aaaaaaa666666aaaaa666666666666666666666666666666666666666666aaaaaaaaaa6666666666666
                6666666666666666666aaa6666666666666666666a11aaaaaa666666666666666666666666666a11aaaa66666aaaaaaa66666666666666666666aa6666666666666666666aa1a1aaaaa6666666666666
                666666666666666666aaaaa666666666666666666aaaaaaa1a666666666666666666666666666aaaaaaa66666aaaaaaa6666666666666666666aaaa666666666666666666aaaaaa11aa6666666666666
                66666666666666666aaaaaa666666666666666666aaaaaaaaa6666666666a66666666aaaaa666a1aaaaa66666aaaaaaa66666666666666666aaaaaa666666666666666666aaaaaaaaaa6666666666666
                66666666666666666aaa1a666666a666666666666aaaaaaaaa666666666aa66666666aaaaa666aaaaaaa66666aaaaaaa66666666666666666aaa1a666666aa66666666666aaaa1aaaaa66666666aa666
                66666666666666666aaaaaa66666a666666666666aaaaaaa1a666666666aa66666666aaaaa666aaaaaaa66666aaaaaaa66666666666666666aaaaaa66666aa66666666666aaaaaaa1aa66666666aa666
                66666666aaa666666aa11a66666aaa66666666666aaaaaaaaa66aaaaaa6aa63666666aaaaa666aaaaaaa66666aaaaaaa666666666aa666666aaa1a66666aaa66666666666aaaaaaaaaa6aaaaaaaaa666
                a6aa6666aaaaaaaaaaa1aaa666aaaaa6666666666aaaaaaa1a66a11aaa6aa666666666aa1aa66aaaaaaa666aaaaaaaaaa6aa6666aaaaaaaaaaaaa1a6666aaaa6666666666aaaaaa11aa6a11aaaaaa666
                aaaa66666a1aa1aaaaaaaaa666aaaaa6666666666aaaaaaaaa66aaaa1a6aa66666666aaaaaa66aa1aaaa666aaaaaaaaaaaaa6666aa1aaa1aaaaaaaa6666aaaa6666666666aaaaaaaaaa6aaaa1aaaa666
                aa1a66666aaa1111aaaaaaa666aaaaa6666666666aaaaaaaaa66aaaa1aaaa66666666aaaaaa66aaaaaaa666aaaaaaaaaaa1a6666aaaa1a11aaaaaaa6666aaaa6666666666aaaaaaaaaa6aaaa1aaaa666
                aaaa6666aaaaaaaaaaaaaaaa66aaaaaa66aa6aa6aaaaaaaaaaa6a11aaaaaa66666666aaaaaa66aaaaaaa666aaaaaaaaaaaaa6666aaaaaaaaaaaaaaaa66aaaaaa666a66aaaaaaaaaaaaa6a11aaaaaa666
                aa1a6666aaaaaaaaaaaaaaaa66aaaaaa66aaaaaaaaaaaaaaaaa6aaaaaaaaa66a66a66aaaaaa66aaaaaaa666aaaaaaaaaaa1a6666aaaaaaaaaaaaaaaa66aaaaaa666aaaaaaaaaaaaaaaa6aaaaaaaaa666
                aaaaa6aa1a1aaaaaaaaaaaaa66aaaaaaa6aaaa11aaaaaaaaaaaaa11ccaaaaaaa6aaa66aa1aa66aaaaaaa666aaaaaaaaaaaaaaa6aaa1aaaaaaaaaaaaa66aaaaaaa666a11aaaaaacaaaaaaa11cccaaa6aa
                aaaaa6aaaaaaaaaaaaaaaaaaaa1aaaaaa6aaaaaaaaacccaaaaaaaaacccaaaaaa6aaa6aaaaaa66aaaaaaa666aaaaaaaaaaaaaaa6aaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaaaaaccaaaaaaaaacccaaa6aa
                aaaaa6aaaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaaaacccaaaaaaaaacccaaaaaaaaaaaaaaaaaaaaaaaaaa666aaaaaaaaaaaaaaa6aaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaaaaaccaaaaaaaaacccaaaaaa
                aaaaa6aaaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaacccccccaaaaaacccccaaaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaaaaaaaaaa6aaaaaaaaaaaaaaaaaaaaaaaaaa6a1aaaaaacccccccaaaaacccccaaaaa
                aaaaacccccccccaaaaaaaaaaaaaaaaaaa6aaaaaaacccccccaaaaaacccccaaaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaaaaaaaaaccccccccccaaaaaaaaaaaaaaaaaa6aaaaaaaacccccccaaaaacccccaaaaa
                aaaaacccccccccaaaaaaaaaaaaaaaaaaa6aaaaaaacccccccaaaaaacccccaaaaaaaaaaaaaaaaaaaaaaaaaaa6aaaaaaaaaaaaaaccccccccccaaaaaaaaaaaaaaaaaa6aaaaaaaacccccccaaaaacccccaaaaa
                aaaaacddccccccaaaaaaaaaaaaaaaaaaa6aaaaaaacddccccaaaaacccccccaa111aaaaaaaaaaaaaaaccaaaa6aaaaaaaaaaaaaaccdcdcccccaaaaaaaaaaaaaaaaaa6aaaaaaaacccccccaaaacccccccc11a
                aaaaacccccccdcaaaaaaaaaaaaaaaaaaa6aaaaaaacccccccaaaaacccccccaaa11aaaaaaaaaaaaaaccccaaa6aaaaaaaaaaaaaaccccccddccaaaaaaaaaaaaaaaaaa6aaaaaaaacccccccaaaaccccccccaaa
                aaaaacccccccccaaaaaaaaaacaaaaaaaacccccaaacdcccccaaaaacccccccaaaaaaaaaaa1aaaaaccccccaaa6aaaaaaaaaaaaaaccccccccccaaaaaaaaaaaaaaaaaaaccccaaaacccdcccaaaaccccccccaaa
                aaaaacccccccccaaaaaaaaaccaaaaaaaacccccaaacccccccaaaaacccccccaa1aaaaaaaaaaaaaacccdcaaaaaaccaaaaaaaaaaaccccdcccccaaaaaaaaccaaaaaaaaaccccaaaacccdcccaaaacccccccca1a
                aaaaacccccccdcaaaaaaaaaccaaaaaaaacccccaaacccccccaaaaacccccccaa111aaaaaaaaaaaaccccccaaaaaccaaaaaaaaaaacccccccdccaaaaaaaaccaaaaaaaaccccccaaacccccccaaaacccccccc11a
                aaaaacccccccccaaccccccaccaaaaaaaacccccaaacccccccaaaaacccccccaaaaaaaaacc1aaaaacccdcaaaaacccaaaaaaaaaaaccccccccccacccccccccaaaaaaaaccccccaaacccdcccaaaaccccccccaaa
                aaaaacccccccdcaacddcccaccaaaaaaaaaccdccaacccccccaaaccccccccccaccaaaacccccccccccccdcaaaaccccaaaaaaaaaaccccccddccacddccccccaaaaaaaacccccccaacccccccaaccccccccccccc
                aaaaacccccccccaaccccdcaccaaaaaaaaccccccaaccdccccaaacccccccccccccaaaaccdcccdccccccccaaaaccccaaaaaaaaaaccccccccccaccccdccccaaaaaaaacccccccaaccccdccaaccccccccccccc
                aaaaacccccccccaaccccdccccaaaaaaaaccccccaacccccccaaacccccccccccdcaaaaccccdcddcccccccaaaaccccaaaaaaaaaaccccccccccaccccdccccaaaaaaaacccccccaacccccccaaccccccccccccc
                accacccccccccccacddccccccaaaaaaaaccccccaacccccccaaacccccccccccccaaaaccccccccccccccccaaccccccaaacaacccccccccccccacddccccccaaaaaaaacccccccaacccccccaaccccccccccccc
                cccccccccccccccacccccccccaacaacaaccccccaacccccccaaacccccccccccdcaaaaccccccccccccccccaaccccccaaaccccccccccccccccacccccccccaaaaacaacccccccaacccccccaaccccccccccccc
                ccddcccccccccccccddddcccccccacccaaccdccaacccccccaaacccccccccccccccacccdcccccccccccccaacccccccaaacddccccccccccccccddcdccccaccacccacccccccaacccccccaaccccccccccccc
                ccccccccccccccccccccccccccccacccaccccccaacccccccaaacccccccccccccccaccccccccccccccccccccccccccacccccccccccccccccccccccccccaccacccccccccccaaccccdccaaccccccccccccc
                ccccccccccccccccccccccccccccccccccccccccccccccccaaacccccccccccccccaccccccccccccccccccccccccccacccccccccccccccccccccccccccccccccccccccccccccccccccaaccccccccccccc
                ccccccccccccccccccccccccccccccccccccccccccccccccccacccccccccccccccaccccccccccccccccccccccccccacdccccccccccccccccccccccccccccccccccccccccccccccccccaccccccccccccc
                ccccccccccccccccccccccccccccccccccccccccccccccccccacccccccccccccccaccccccccccccccccccccccccccaccccccccccccccccccccccccccccccccdcccccccccccccccccccaccccccccccccc
                ccccccccccccccccccccccccccccccccccccccccccccccccccacccccccccccccccaccccccccccccccccccccccccccaccccccccccccccccccccccccccccccccccccccccccccccccccccaccccccccccccc
                ccccccccccccccccccccccccccdddcccccccccccccccccccccacccccccccccccccaccccccccccccccccccccccccccacccccccccccccccccccccccccccddcdcdccccccccccccccccccccccccccccccccc
                cccccccccccccccccccccccccccddcccccccccccccccccccccacccccccccccccccaccccccccccccccccccccccccccaccccccccccccccccccccccccccccccdcdccccccccccccccccccccccccccccccccc
                cccccccccccccccccccccccccccccccccccdccccccccccccccacccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccdccccdcccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccdcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccdccccccccccccccccccccccccccccccccccccc
                ccccccccccccccccccccccccccdddccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccddcdccccccccccccccccccccccccccccccccccc
                cccccccccccccccccccccccccccccccccccdcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
                cccccccccccccccccdccccccccccccccccdccccccccccccccccccccccdccccccccccccccccdccccccccccccccccccccccdccccccccccccccccdccccccccccccccccccccccdccccccccccccccccdccccc
                ccccccdcccddcccccddccccdcccdccccdcddcccdccccccdcccddcccccddccccdcccdccccdcddcccdccccccdcccddcccccddccccdcccdccccdcddcccdccccccdcccddcccccddccccdcccdccccdcddcccd
                ccdcccddcddccdcccddcccddcccddcccdccddcddccdcccddcddccdcccddcccddcccddcccdccddcddccdcccddcddccdcccddcccddcccddcccdccddcddccdcccddcddccdcccddcccddcccddcccdccddcdd
                ccddccddcddccddcccddcddccccddcdcddcddddcccddccddcddccddcccddcddccccddcdcddcddddcccddccddcddccddcccddcddccccddcdcddcddddcccddccddcddccddcccddcddccccddcdcddcddddb
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
    StatusBarFunc()
    info.set_score(ScorePre)

def on_on_overlap2(sprite3, otherSprite):
    otherSprite.destroy(effects.confetti, 500)
    music.ba_ding.play()
    info.change_score_by(20)
    scene.camera_shake(2, 100)
sprites.on_overlap(SpriteKind.player, SpriteKind.Reward, on_on_overlap2)

def StatusBarFunc():
    global statusbar
    statusbar = statusbars.create(20, 4, StatusBarKind.energy)
    statusbar.value = 0
    statusbar.set_color(8, 1)
    statusbar.max = 30
    statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
    statusbar.attach_to_sprite(Hero)

def on_on_overlap3(sprite32, otherSprite3):
    global ResourceAmount
    otherSprite3.destroy(effects.confetti, 500)
    ResourceAmount += 1
    music.ba_ding.play()
    info.change_score_by(10)
    scene.camera_shake(2, 100)
    statusbar.value = ResourceAmount
sprites.on_overlap(SpriteKind.player, SpriteKind.Resource, on_on_overlap3)

def on_overlap_tile2(sprite2, location2):
    global ScorePre, Spectate, Spectator
    ScorePre = info.score()
    Spectate += 1
    Spectator = sprites.create(assets.image("""
            myImage7
        """),
        SpriteKind.SpectatorSprite)
    Spectator.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
    Spectator.set_flag(SpriteFlag.GHOST_THROUGH_TILES, True)
    Spectator.set_flag(SpriteFlag.SHOW_PHYSICS, False)
    Spectator.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    Spectator.set_position(Hero.x, Hero.y)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Reward)
    scene.set_background_image(img("""
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
    """))
    scene.camera_follow_sprite(Spectator)
    controller.move_sprite(Spectator, 100, 100)
    
    def on_start_cutscene2():
        story.print_dialog("Spectating. Press B to exit.", 80, 90, 50, 150)
        story.cancel_current_cutscene()
    story.start_cutscene(on_start_cutscene2)
    
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile2)

def start_level():
    if current_level == 0:
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
    elif current_level == 1:
        effects.blizzard.start_screen_effect()
        tiles.set_current_tilemap(tilemap("""
            level5
        """))
    elif current_level == 2:
        tiles.set_current_tilemap(tilemap("""
            level18
        """))
    elif current_level == 3:
        tiles.set_current_tilemap(tilemap("""
            level
        """))
    else:
        game.game_over(True)

def on_life_zero():
    game.over(False, effects.melt)
info.on_life_zero(on_life_zero)

def BKeyPressed(OnShield: bool):
    global ShieldStatus, myDart, ResourceAmount
    if OnShield:
        Hero.set_image(assets.image("""
            myImage3
        """))
        ShieldStatus += -1
        myDart = darts.create(assets.image("""
            myImage5
        """), SpriteKind.projectile)
        myDart.set_position(Hero.x, Hero.y)
        myDart.pow = 80
        myDart.angle = AngleShield
        myDart.angle_rate = 1
        myDart.set_flag(SpriteFlag.DESTROY_ON_WALL, True)
        myDart.throw_dart()
    elif ResourceAmount < 1:
        game.splash("Get More Resources")
    else:
        if AngleShield == 10:
            Hero.set_image(assets.image("""
                myImage2
            """))
        else:
            Hero.set_image(assets.image("""
                myImage8
            """))
        ShieldStatus += 1
        ResourceAmount += -1
        statusbar.value = ResourceAmount
    RefreshStatus()
def Init():
    global ShieldStatus, ResourceAmount, i
    info.set_life(3)
    info.set_score(0)
    game.set_game_over_playable(False, music.melody_playable(music.wawawawaa), False)
    game.set_game_over_playable(True, music.melody_playable(music.power_up), False)
    ShieldStatus = 0
    ResourceAmount = 0
    i = 0
def Damage():
    global ShieldStatus
    Hero.set_velocity(0, -100)
    if ShieldStatus == 1:
        Hero.set_image(assets.image("""
            myImage0
        """))
        ShieldStatus += -1
    else:
        info.change_life_by(-1)
    scene.camera_shake(2, 200)

def on_overlap_tile3(sprite22, location22):
    global current_level
    current_level += 1
    start_level()
    Level_Spawn_Points()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite6, location5):
    game.over(False, effects.dissolve)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile9
    """),
    on_overlap_tile4)

myDart: Dart = None
Spectator: Sprite = None
statusbar: StatusBarSprite = None
ScorePre = 0
AngleShield = 0
i = 0
canDoubleJump = False
ResourceAmount = 0
myEnemy: Sprite = None
Resource2: Sprite = None
Reward2: Sprite = None
Hero: Sprite = None
ShieldStatus = 0
Spectate = 0
current_level = 0
Starting_Game_Mechanics()
current_level = 3
start_level()
Level_Spawn_Points()
Init()
StatusBarFunc()

def on_update_interval():
    global canDoubleJump
    if Hero.is_hitting_tile(CollisionDirection.BOTTOM):
        canDoubleJump = True
    RefreshStatus()
game.on_update_interval(100, on_update_interval)
