<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="less">
@font-face
{
    font-family: chinese_font;
    src: url(./assets/chinese_font.ttf);
}

@font-face
{
    font-family: gillsans_;
    src: url(./assets/GillSansMT.ttf);
}

@font-face
{
    font-family: gillsans_light;
    src: url(./assets/gillsans_light.ttf);
}


body{
    margin: 0;
    padding: 0;
    font-size: 16px;
    font-family: 'gillsans_';
    letter-spacing: 1px;
    // line-height: 25px;
    // user-select: none;
    // font-weight:100;
	// user-select:none;
}




</style>
