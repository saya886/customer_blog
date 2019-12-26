<template>
  <div class="main">
      <div class="sec">
          <div class="ubclock_txt">ubclock</div>
          <div class="main_item">
              <div class="detail_button">See Deatils</div>
              
              <div class="icon_key"><img style="margin-top:10px" src="../assets/img_19.png" alt=""> <span class="sec_index">01</span> </div>
              
          </div>
            <div class="move_text text_1">Business Hub</div>
            <div class="move_text text_2">China</div>

            <div class="text_1_"></div>
            <div class="text_2_"></div>
            
      </div>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="less" scoped>
.main{
    height: 1050px;
    background: gray;
    // padding-top:200px; 
    
}
.sec{
    height: 800px;
    
    padding-top:350px; 
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content:space-between;
    background: rgb(255, 255, 255);
    border-bottom:2px solid rgb(48, 48, 48);
}
.sec:hover{
    .move_text{
        transform: translate(0px, 50px);
    }
    
}
.main_item{
    // position: absolute;
    z-index: 10;
    height: 400px;
    width: 40%;
    margin: 0 auto;
    box-shadow: 0px 0px 30px 10px grey;
    background: gray;
    background:url("../assets/img_18.png") no-repeat center center;
    background-size: cover;
    position: relative;
    
}
.text_1{
    z-index: 1;
    position: absolute;
    font-size: 230px;
    bottom: 250px;
    left: -40px;
    font-family: gillsans_light;
    transition-duration: 0.6s;
    transition-timing-function: cubic-bezier(0.165, 0.84, 0.44, 1);
    transform: translate(0px, -200px);
    // display: none;
}
.text_2{
    z-index: 1;
    position: absolute;
    font-size: 230px;
    top: 150px;
    right: -10px;
    font-family: gillsans_light;
    transition-duration: 0.6s;
    transition-timing-function: cubic-bezier(0.165, 0.84, 0.44, 1);
    transform: translate(0px, -200px);
    // display: none;
    
}
.text_1_{
    z-index: 1;
    position: absolute;
    height: 250px;
    bottom: 450px;
    background: rgb(255, 255, 255);
    width: 100%;
}
.text_2_{
    z-index: 1;
    position: absolute;
    height: 200px;
    top: -55px;
    background: rgb(255, 255, 255);
    width: 100%;
    border-top:2px solid rgb(65, 65, 65);
}
.detail_button{
    z-index: 1;
    position: absolute;
    font-size: 30px;
    bottom: 30px;
    right: -200px;
    font-family: gillsans_light;
    color: gray;
    cursor: pointer;
}
.icon_key{
    position: absolute;
    top: -50px;
    left:-150px;
    
}
.sec_index{
    font-size: 16px;
    color: gray;
    margin-left:10px; 
}
.ubclock_txt{
    position: absolute;
    left: 100px;
    top: 200px;
    font-size: 30px;
    font-family: gillsans_light;
    color: gray;
    transform: rotate(90deg);
}
.detail_button:hover{
    text-shadow: 0px 0px 20px #b1b1b1;
    color: rgb(31, 31, 31);
}

</style>