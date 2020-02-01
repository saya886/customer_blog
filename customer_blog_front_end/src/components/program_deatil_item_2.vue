<template>
  <div class="main">
    <div class="title">CuratedChina</div>
    <div class="dvider"></div>
    <div class="content">{{ $t('b_1_4')}}<br>
{{ $t('b_1_5')}}<br>
{{ $t('b_1_6')}}</div>
    <div @click="change_route('contact#enquire')" class="center_button">{{ $t('b_1_7')}}</div>
  </div>
</template>

<script>
export default {
data(){
  return{

  }
},
mounted(){

},
methods:{
change_route(path){
            this.$router.push("/" + path)
        }
}
}
</script>

<style lang="less" scoped>
.main{
    height: 450px;
    background:url("../assets/img_43.jpg") no-repeat center center;
    background-size: cover;
    padding-top: 130px;

}
.title{
  text-align:center;
  font-size: 24px;
  color: white;
  
  text-align: center;
  font-family: gillsans_light;
  letter-spacing: 1px;
  padding-bottom: 20px;
}
.content{
  padding-top: 40px;
  text-align:center;
  font-size: 16px;
  color: white;
  line-height: 40px;
  text-align: center;
  font-family: gillsans_light;
  letter-spacing: 2px;
}
.center_button{
    height: 35px;
    width: 230px;
    margin: 0 auto;
    margin-top: 70px; 
    
    text-align: center;
    border:2px solid white;
    line-height: 35px;
    font-size: 16px;
    color: white;
    cursor:pointer;
    letter-spacing: 1px;
    
}
.center_button:hover{
    background: white;
    color: black;
}
.dvider{
  border-bottom:2px solid white;
  width:150px;
  margin:0 auto;
}
</style>