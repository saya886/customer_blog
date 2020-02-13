<template>
  <div class="main">
      <div  v-bind:id="program.id + '_id'" v-for="program in data_list" class="sec">
          <div class="ubclock_txt">Unlock</div>
          <div class="main_item">
              <div @click="go_to_detail(program.id)" class="detail_button">{{ $t('p_1_1')}}</div>
              <img @click="go_to_detail(program.id)" class="icon" v-bind:src="program.program_img" alt="">
              <div class="icon_key"><img style="margin-top:10px;display:inline;" src="../assets/img_19.png" alt=""> <span class="sec_index">{{program.id}}</span> </div>
              
          </div>
            <div  :style="text_1_style" class="move_text_1 text_1">{{program.title_1}}</div>
            <div :style="text_1_style" class="move_text_2 text_2">{{program.title_2}}</div>
            <div class="text_1_"></div>
            <div class="text_2_"></div>
      </div>
      <div ></div>
  </div>
</template>

<script>
export default {
    data(){
        return{
            "data_list":[],
            "text_1_style":{},
            "text_2_style":{},
        }
    },
    mounted (){
        this.$axios({
            method: "get",
            url: "/program/",
        }).then(response => {
            console.log(response, "success");   // 成功的返回
            this.data_list = response["data"]["data"]

            var userAgentInfo = navigator.userAgent;
            var Agents = new Array("Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod");  
            var flag = true;
            for (var v = 0; v < Agents.length; v++) {  
                if (userAgentInfo.indexOf(Agents[v]) > 0) { flag = false; break; }  
            }
            if(!flag){
                this.text_1_style = {"transform": "translate(0px, 1px)"}
                this.text_2_style = {"transform": "translate(0px, 1px)"}
            }
            
        })
        .catch(error => {
            console.log(error, "error")
        }); // 失败的返回

        
    },
    methods:{
        go_to_detail(program_id){
            console.log(program_id);
            this.$router.push("/programs/"+program_id.toString())
        }
        
    },
    updated (){
        console.log("commp updated")
        if(location.hash  != ""){
            document.getElementById('1_id').scrollIntoView();
        }

        
        
    }
}
</script>

<style lang="less" scoped>
.main{
    // height: 1050px;
    background: gray;
    // padding-top:200px; 
    
}
.sec{
    height: 500px;
    
    padding-top:200px; 
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content:space-between;
    background: rgb(255, 255, 255);
    border-bottom:2px solid rgb(48, 48, 48);
    border-top:2px solid rgb(65, 65, 65);
}
.sec:hover{
    .move_text_1{
        transform: translate(0px, 1px);
    }
    .move_text_2{
        transform: translate(0px, 1px);
    }
    
}
.main_item{
    // position: absolute;
    z-index: 10;
    height: 300px;
    width: 40%;
    margin: 0 auto;
    box-shadow: 0px 0px 30px 10px grey;
    background: gray;
    // background:url("../assets/img_18.png") no-repeat center center;
    // background-size: cover; 
    position: relative;
    
    
}
.text_1{
    z-index: 1;
    position: absolute;
    font-size: 150px;
    bottom: 50px;
    left: -40px;
    font-family: gillsans_light;
    transition-duration: 0.6s;
    transition-timing-function: cubic-bezier(0.165, 0.84, 0.44, 1);
    transform: translate(0px, -150px);
    // display: none;
    // background:red;
}
.text_2{
    z-index: 1;
    position: absolute;
    font-size: 150px;
    top: 80px;
    right: -10px;
    font-family: gillsans_light;
    transition-duration: 0.6s;
    transition-timing-function: cubic-bezier(0.165, 0.84, 0.44, 1);
    transform: translate(0px, 150px);
    // display: none;
    // background:red;
    
}
.text_1_{
    z-index: 1;
    position: absolute;
    height: 150px;
    bottom: 200px;
    background: rgb(255, 255, 255);
    width: 100%;
}
.text_2_{
    z-index: 1;
    position: absolute;
    height: 150px;
    top: 200px;
    background: rgb(255, 255, 255);
    width: 100%;
    
}

.detail_button{
    z-index: 1;
    position: absolute;
    font-size: 20px;
    bottom: 30px;
    right: -200px;
    font-family: gillsans_light;
    color: gray;
    cursor: pointer;
    transition-duration: 0.6s;
    transition-timing-function: cubic-bezier(0.165, 0.84, 0.44, 1);
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
    z-index:10000;
}
.detail_button:hover{
    text-shadow: 0px 0px 20px #b1b1b1;
    color: black;
    transform: scale(1.5,1.5);
}
.icon{
    width:100%;
    object-fit: cover;
    // max-width:100%;
    height:300px;
    cursor: pointer;
}

</style>