<template>
  <div class="main">
      <div class="sec">
          <div class="main_item">
              <div class="left">=</div>
              <div class="right">
                  
              </div>
              <img class="logo_center" src="../assets/logo_dark.png" alt="">
              <div class="title_1">WHO WE ARE</div>
              <div class="title_2">Curated China</div>
              <div class="title_3">▶</div>

              <div class="text_div_1">
                    <span class="big_one">U</span>
                    <span class="small_one">s</span>
                </div>
            <div class="text_div_2">
                      <span class="big_one">A</span>
                      <span class="small_one">     bout</span>
                  </div>

            <img class="icon_key" src="../assets/icon_key.png" alt="">
          </div>
      </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.main{
    background: gray;
    // padding-top:200px; 
}
.sec{
    height: 1000px;
    background: gray;
    padding-top:200px; 
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content:space-between;
    background: rgb(248, 248, 248);
    border-bottom:2px solid rgb(255, 255, 255);
}
.sec::before{
    content: "";
    height: 100%;
    width: 50%;
    background: rgb(49, 49, 49);
    position: absolute;
    top: 0;
    right: 0;
    z-index: 0;
}
.main_item{
    // position: absolute;
    z-index: 10;
    height: 720px;
    
    background: white;
    background:url("../assets/img_20.png") no-repeat center center;
    background-size: cover;
    width: 70%;
    margin: 0 auto;
    box-shadow: 0px 0px 30px 10px grey;
    position: relative;
}
.text_1{
    z-index: 1;
    position: absolute;
    font-size: 300px;
    bottom: 20px;
    left: 20px;
}
.text_2{
    z-index: 1;
    position: absolute;
    font-size: 300px;
    top: 20px;
    right: 20px;
}
.left{
    height: 137px;
    width: 137px;
    position: absolute;
    left: 0px;
    top: 0px;
    background: rgb(83, 83, 83);
    font-size: 80px;
    color: white;
    line-height: 160px;
    text-align: center;
    font-family: gillsans_light;
}
.right{
    width: 137px;
    height: 100%;
    position: absolute;
    right: 0px;
    background: rgb(83, 83, 83);
}
.logo_center{
    width: 200px;
    margin: 0 auto;
    margin-top:60px; 
    display: block;

}
.title_1{
    font-size: 48px;
    color: rgb(83, 83, 83);
    margin-top: 170px;
    text-align: center;
}
.title_2{
    font-size: 18px;
    color: rgb(83, 83, 83);
    margin-top: 30px;
    text-align: center;
}
.title_3{
    font-size: 30px;
    color: rgb(83, 83, 83);
    margin-top: 45px;
    text-align: center;
}
.text_div_2{
    position: absolute;
    left: 300px;
    bottom: 50px;
    .big_one{
        font-size: 80px;
        color: rgb(83, 83, 83);
        font-family: gillsans_light;
    }
    .small_one{
        font-size: 25px;
        color: rgb(83, 83, 83);
        font-family: gillsans_light;
    }
}
.text_div_1{
    position: absolute;
    right: 35px;
    bottom: 100px;
    .big_one{
        font-size: 80px;
        color: white;
        font-family: gillsans_light;
    }
    .small_one{
        font-size: 25px;
        color: white;
        font-family: gillsans_light;
    }
}
.icon_key{
    position: absolute;
    left: 100px;
    top: 300px;
}
</style>