#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/NasusUlt/NasusUlt.bin"
    "DATA/Characters/Nasus/Animations/Skin0.bin"
    "DATA/Characters/NasusUlt/NasusUlt.bin"
    "DATA/Characters/Nasus/Animations/Skin16.bin"
}
entries: map[hash,embed] = {
    "Characters/NasusUlt/Skins/Skin16" = SkinCharacterDataProperties {
        championSkinName: string = "BaseNasusUlt"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Nasus/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Nasus/Skins/Base/Nasus.skl"
            simpleSkin: string = "ASSETS/Characters/Nasus/Skins/Base/Nasus.skn"
            texture: file = "assets/characters/nasus/skins/base/nasus.tex"
	 	 	skinScale: f32 = 2
            selfIllumination: f32 = 0.5
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            initialSubmeshToHide: string = "Sun_Mat, Sun_Sword_Mat, Sun_Shield_Mat, Sun_Glasses_Mat"
            submeshRenderOrder: string = "Leona_Mat, Hair"
        }
        armorMaterial: string = "Metal"
        defaultAnimations: list[string] = {
            "Idle1_BOOMBOX"
        }
        iconCircle: option[file] = {
            "assets/characters/nasusult/hud/nasus_circle.tex"
        }
        iconSquare: option[file] = {
            "assets/characters/nasusult/hud/nasus_square.tex"
        }
        mResourceResolver: link = "Characters/NasusUlt/Skins/Skin0/Resources"
        objectPath: hash = "Characters/NasusUlt/Skins/Skin0"
    }
    "Characters/NasusUlt/Skins/Skin16/Resources" = ResourceResolver {}
}
