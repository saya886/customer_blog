<template>
  <div class="main">
      <div class="sec">
          <div class="main_item">
              <div class="left">2.</div>
              <img class="logo_center" src="../assets/logo_dark.png" alt="">
              <div class="title_1">{{ $t('a_5')}}</div>
              <div class="title_2">{{ $t('a_6')}}</div>
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
    height: 800px;
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
    height: 500px;
    
    background: white;
    background-size: cover;
    width: 60%;
    margin: 0 auto;
    box-shadow: 0px 0px 30px 10px grey;
    position: relative;
}
.left{
    height: 200px;
    width: 90px;
    position: absolute;
    left: 0px;
    top: 0px;
    background: rgb(83, 83, 83);
    font-size: 50px;
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
    font-size: 20px;
    color: rgb(83, 83, 83);
    margin-top: 35px;
    text-align: center;
    font-family: gillsans_light;
}
.title_2{
    font-size: 15px;
    color: rgb(83, 83, 83);
    font-family: gillsans_light;
    width: 75%;
    height: 340px;
    margin: 0 auto;
    margin-top: 60px;
    line-height: 23px;
    text-align:justify;
    overflow-y: hidden;
    // letter-spacing:1px;
}

</style>