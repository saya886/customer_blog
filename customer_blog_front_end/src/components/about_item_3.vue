<template>
  <div class="main">
      <div class="sec">
          <div class="main_item">
              <div class="left">=</div>
              <img class="logo_center" src="../assets/logo.png" alt="">
              <div class="title_1">CORPORATE  VALUES</div>

              <div class="title_2">
                <div class="left_">Genuine</div>
                <div class="right_">Innovation</div>
              </div>
              <div class="title_2">
                <div class="left_">Trustworthy</div>
                <div class="right_">Diversity</div>
              </div>
              <div class="title_2">
                <div class="left_">Detail oriented</div>
                <div class="right_">Entrepreneurial spirit</div>
              </div>

              <div class="a_1">V</div>
              <div class="a_2">L</div>
              <div class="a_3">A</div>
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
    background:url("../assets/img_21.png") no-repeat center center;
    background-size: cover;
    width: 70%;
    margin: 0 auto;
    box-shadow: 0px 0px 30px 10px grey;
    position: relative;
}
.left{
    height: 300px;
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
.logo_center{
    width: 200px;
    margin: 0 auto;
    margin-top:60px; 
    display: block;

}
.title_1{
    font-size: 40px;
    color: rgb(255, 255, 255);
    margin-top: 45px;
    text-align: center;
    font-family: gillsans_light;
    letter-spacing:8px;
    margin-bottom: 70px;
}
.title_2{
    width: 70%;
    margin: 0 auto;
    margin-bottom:45px; 
    .left_{
      display: inline-block;
      font-size: 24px;
      color: rgb(221, 221, 221);
      font-family: gillsans_light;
      width: 50%;
      text-align: right;
      transform:translate(-60px,0px);
      letter-spacing:1px;
    }
    .right_{
      display: inline-block;
      font-size: 24px;
      color: rgb(214, 214, 214);
      font-family: gillsans_light;
      width: 50%;
      text-align: left;
      transform:translate(60px,0px);
      letter-spacing:1px;
    }
}
.a_1{
  color: rgb(221, 221, 221);
  font-size: 125px;
  font-family: gillsans_light;
  position: absolute;
  left: 144px;
  bottom: 200px;
}
.a_2{
  color: rgb(221, 221, 221);
  font-size: 125px;
  font-family: gillsans_light;
  position: absolute;
  left: 600px;
  bottom: 75px;
}
.a_3{
  color: rgb(221, 221, 221);
  font-size: 125px;
  font-family: gillsans_light;
  position: absolute;
  right: 150px;
  top: 150px;
}
</style>