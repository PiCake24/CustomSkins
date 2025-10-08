#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/NasusUlt/NasusUlt.bin"
    "DATA/Characters/Nasus/Animations/Skin0.bin"
    "DATA/Characters/NasusUlt/NasusUlt.bin"
    "DATA/Characters/NasusUlt/Animations/Skin45.bin"
}
entries: map[hash,embed] = {
    "Characters/NasusUlt/Skins/Skin51" = SkinCharacterDataProperties {
        championSkinName: string = "BaseNasusUlt"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Nasus/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Nasus/Skins/Base/Nasus.skl"
            simpleSkin: string = "ASSETS/Characters/Nasus/Skins/Base/Nasus.skn"
            texture: string = "ASSETS/Characters/Nasus/Skins/Base/Nasus.tex"
	 	 	skinScale: f32 = 2
            selfIllumination: f32 = 0.5
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            initialSubmeshToHide: string = "Leona_Mat, Shield_Mat, Sun_Glasses_Mat"
            submeshRenderOrder: string = "Sun_Mat, Hair"
        }
        armorMaterial: string = "Metal"
        defaultAnimations: list[string] = {
            "Idle1_BOOMBOX"
        }
        iconCircle: option[string] = {
            "ASSETS/Characters/NasusUlt/HUD/Nasus_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/NasusUlt/HUD/Nasus_Square.tex"
        }
        mResourceResolver: link = "Characters/NasusUlt/Skins/Skin0/Resources"
    }
    "Characters/NasusUlt/Skins/Skin51/Resources" = ResourceResolver {}
}
