namespace SpriteKind {
    export const Coin = SpriteKind.create()
    export const Health = SpriteKind.create()
    export const Reward = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function (sprite, location) {
    game.over(false, effects.slash)
    music.wawawawaa.playUntilDone()
})
function Variables_Init () {
    BookPossesion_Enchiridion = false
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite8, otherSprite2) {
    otherSprite2.destroy(effects.ashes, 100)
    info.changeLifeBy(-1)
    scene.cameraShake(2, 200)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile12`, function (sprite4, location3) {
    BookPossesion_Enchiridion = true
    scene.cameraShake(4, 500)
    story.printCharacterText("You got a book.")
})
function Level_Spawn_Points () {
    // This is a spawn point on the tilemap for the hero. This tile will be replaced by the hero sprite
    for (let value of tiles.getTilesByType(assets.tile`Hero Spawn Point`)) {
        tiles.placeOnTile(Hero, value)
        tiles.setTileAt(value, assets.tile`transparency16`)
    }
    // This is a spawn point for rewards. This tile will be replaced by your reward sprite. The art should be replaced with yours.
    for (let value2 of tiles.getTilesByType(assets.tile`Reward Spawn`)) {
        let RewardVariable: Sprite = null
        tiles.placeOnTile(RewardVariable, value2)
        tiles.setTileAt(value2, assets.tile`transparency16`)
    }
}
function Starting_Game_Mechanics () {
    Hero = sprites.create(assets.image`myImage0`, SpriteKind.Player)
    scene.cameraFollowSprite(Hero)
    controller.moveSprite(Hero, 100, 0)
    Hero.ay = 200
    canDoubleJump = true
    info.setScore(0)
    info.setLife(3)
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Hero.vy == 0) {
        Hero.vy = -100
    }
    if (Hero.isHittingTile(CollisionDirection.Bottom)) {
        Hero.vy = -180
    } else if (canDoubleJump) {
        Hero.vy = -100
        canDoubleJump = false
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Reward, function (sprite3, otherSprite) {
    otherSprite.destroy(effects.confetti, 500)
    music.baDing.play()
    info.changeScoreBy(1)
    scene.cameraShake(2, 100)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardWater, function (sprite6, location5) {
    game.over(false, effects.slash)
    music.wawawawaa.playUntilDone()
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestOpen, function (sprite7, location6) {
    game.over(true, effects.confetti)
    music.powerUp.play()
    info.changeScoreBy(1)
})
function start_level () {
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    sprites.destroyAllSpritesOfKind(SpriteKind.Reward)
    if (current_level == 0) {
        // This will be your "platform" for level 1. Start with designing this to create your world. You can use the pre-made gallery tiles or create your own.
        tiles.setCurrentTilemap(tilemap`level1`)
        scene.setBackgroundImage(img`
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
            `)
    } else if (current_level == 1) {
        tiles.setCurrentTilemap(tilemap`level5`)
    } else if (current_level == 2) {
        tiles.setCurrentTilemap(tilemap`level18`)
    } else if (current_level == 3) {
        game.gameOver(true)
    }
}
info.onLifeZero(function () {
    game.over(false, effects.splatter)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite2, location2) {
    current_level += 1
    start_level()
    Level_Spawn_Points()
})
let canDoubleJump = false
let Hero: Sprite = null
let BookPossesion_Enchiridion = false
let current_level = 0
Starting_Game_Mechanics()
current_level = 0
start_level()
Level_Spawn_Points()
game.onUpdate(function () {
    if (Hero.isHittingTile(CollisionDirection.Bottom)) {
        canDoubleJump = true
    }
})
