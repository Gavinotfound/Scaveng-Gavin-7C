namespace SpriteKind {
    export const Coin = SpriteKind.create()
    export const Health = SpriteKind.create()
    export const Reward = SpriteKind.create()
}

scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile0
    `, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    game.over(false, effects.slash)
    music.wawawawaa.playUntilDone()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile
    `, function on_overlap_tile2(sprite2: Sprite, location2: tiles.Location) {
    
    current_level += 1
    start_level()
    Level_Spawn_Points()
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
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
sprites.onOverlap(SpriteKind.Player, SpriteKind.Reward, function on_on_overlap(sprite3: Sprite, otherSprite: Sprite) {
    otherSprite.destroy(effects.confetti, 500)
    music.baDing.play()
    info.changeScoreBy(1)
    scene.cameraShake(2, 100)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile12
    `, function on_overlap_tile3(sprite4: Sprite, location3: tiles.Location) {
    story.startCutscene(function on_start_cutscene() {
        
        story.printDialog("A bag. Open it?", 80, 90, 50, 150)
        story.showPlayerChoices("Yes", "No")
        if (story.checkLastAnswer("Yes")) {
            story.printDialog("You found a book.", 80, 90, 50, 150)
            story.printDialog("Carpenter", 80, 90, 50, 150)
            BagOpened += 1
        } else {
            story.printDialog("Okay.", 80, 90, 50, 150)
            info.setLife(0)
        }
        
        story.cancelCurrentCutscene()
    })
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava1, function on_overlap_tile4(sprite5: Sprite, location4: tiles.Location) {
    game.over(false, effects.melt)
    music.wawawawaa.playUntilDone()
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardWater, function on_overlap_tile5(sprite6: Sprite, location5: tiles.Location) {
    game.over(false, effects.slash)
    music.wawawawaa.playUntilDone()
})
function start_level() {
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    sprites.destroyAllSpritesOfKind(SpriteKind.Reward)
    if (current_level == 0) {
        //  This will be your "platform" for level 1. Start with designing this to create your world. You can use the pre-made gallery tiles or create your own. 
        tiles.setCurrentTilemap(tilemap`
            level1
        `)
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
        tiles.setCurrentTilemap(tilemap`
            level5
        `)
    } else if (current_level == 2) {
        tiles.setCurrentTilemap(tilemap`
            level18
        `)
    } else if (current_level == 3) {
        game.gameOver(true)
    }
    
}

info.onLifeZero(function on_life_zero() {
    game.over(false, effects.melt)
})
function Starting_Game_Mechanics() {
    
    Hero = sprites.create(assets.image`
        myImage0
    `, SpriteKind.Player)
    scene.cameraFollowSprite(Hero)
    controller.moveSprite(Hero, 100, 0)
    Hero.ay = 200
    canDoubleJump = true
    info.setScore(0)
    info.setLife(3)
}

function Level_Spawn_Points() {
    
    //  This is a spawn point on the tilemap for the hero. This tile will be replaced by the hero sprite
    for (let value of tiles.getTilesByType(assets.tile`
        Hero Spawn Point
    `)) {
        tiles.placeOnTile(Hero, value)
        tiles.setTileAt(value, assets.tile`
            transparency16
        `)
    }
    //  This is a spawn point for rewards. This tile will be replaced by your reward sprite. The art should be replaced with yours.
    for (let value2 of tiles.getTilesByType(assets.tile`
        Reward Spawn
    `)) {
        Reward2 = sprites.create(img`
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
            `, SpriteKind.Reward)
        tiles.placeOnTile(Reward2, value2)
        tiles.setTileAt(value2, assets.tile`
            transparency16
        `)
    }
    //  This is a spawn point for rewards. This tile will be replaced by your reward sprite. The art should be replaced with yours.
    for (let value3 of tiles.getTilesByType(assets.tile`
        Enemy Spawn Points
    `)) {
        BadGuy1 = sprites.create(img`
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
            `, SpriteKind.Enemy)
        tiles.placeOnTile(BadGuy1, value3)
        tiles.setTileAt(value3, assets.tile`
            transparency16
        `)
    }
}

scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestOpen, function on_overlap_tile6(sprite7: Sprite, location6: tiles.Location) {
    game.over(true, effects.confetti)
    music.powerUp.play()
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap2(sprite8: Sprite, otherSprite2: Sprite) {
    otherSprite2.destroy(effects.ashes, 100)
    scene.cameraShake(2, 200)
    info.changeLifeBy(-1)
})
let BadGuy1 : Sprite = null
let Reward2 : Sprite = null
let BagOpened = 0
let canDoubleJump = false
let Hero : Sprite = null
let current_level = 0
Starting_Game_Mechanics()
current_level = 0
start_level()
Level_Spawn_Points()
game.onUpdate(function on_on_update() {
    
    if (Hero.isHittingTile(CollisionDirection.Bottom)) {
        canDoubleJump = true
    }
    
})
