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
    font-family: gillsans_light;
    src: url(./assets/gillsans.ttf);
}

* {
    margin: 0;
    padding: 0;
    font-size: 10px;
    font-family: Gill Sans MT Light,chinese_font;
    user-select: none;
    // font-weight:100;
}
div{
  font-size: 1.6rem
}
a{
  text-decoration: none;
}


</style>
