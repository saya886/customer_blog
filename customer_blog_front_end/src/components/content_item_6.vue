<template>
<a id="enquire">
<div class="main">
    <div class="title">ENQUIRE</div>
    <div class="text">A CuratedChina coordinator will reply to you within 24 hours. <br/>We look forward to hearing from you!</div>
    <div class="input_group">
        <div class="input_container">
            <div class="input_lable">
                <div class="input_lable_tip">*</div>
                <div class="input_lable_text">Name :</div>
            </div>
            <!-- <div class="input_item"></div> -->
            <input v-model="name" class="input_item" type="text">
        </div>

        <div class="input_container">
            <div class="input_lable">
                <div class="input_lable_tip">*</div>
                <div class="input_lable_text">Email :</div>
            </div>
            <!-- <div class="input_item"></div> -->
            <input v-model="mail" class="input_item" type="text">
        </div>

        <div class="input_container">
            <div class="input_lable">
                <div class="input_lable_tip input_lable_tip_gray"></div>
                <div class="input_lable_text">Telephone :</div>
            </div>
            <!-- <div class="input_item"></div> -->
            <input v-model="tel" class="input_item" type="text">
        </div>

        <div class="input_container input_container_1">
            <div class="input_lable">
                <div class="input_lable_tip">*</div>
                <div class="input_lable_text">Message :</div>
            </div>
            <!-- <div class="input_item"></div> -->
            <textarea v-model="message" class="textarea_item">
            </textarea>
        </div>
    </div>
    <div class="error_msg">{{error_msg}}</div>
    <div @click="send_enquire()" class="center_cust_button">SEND MY ENQUIRE</div>
    <div class="abs_img_3"></div>
</div>
</a>
</template>

<script>
export default {
    data(){
        return{
            "name":"",
            "mail":"",
            "tel":"",
            "message":"",
            "error_msg":""
        }
    },
    methods:{
        send_enquire(){
            // console.log(this.mail)
            this.error_msg = ""
            if(this.name == "" || this.mail == "" || this.message == ""){
                this.error_msg = this.$t('warn_msg_1')
            }
            let pattern= /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
            if(! pattern.test(this.mail.toString())){
                this.error_msg = this.$t('warn_msg_2')
            }

            if(this.error_msg == ""){
                this.error_msg = ""
                this.$axios({
                    method: "get",
                    url: "/comment/?name="+this.name+"&mail_addr="+this.mail+"&phone="+this.tel+"&content="+this.message,
                }).then(response => {
                    console.log(response, "success");   // 成功的返回 
                    this.error_msg = this.$t('warn_msg_3')    
                })
                .catch(error => {
                    console.log(error, "error")
                    this.error_msg = this.$t('warn_msg_4')  
                }); // 失败的返回
            }
            else{
                
            }
            
            
        }
    }
}
</script>

<style lang="less" scoped>
.main{
    // background: rgba(21, 255, 0, 0.445);
    height: 900px;
    padding: 130px 350px 200px 350px;
    position: relative;
}
.title{
    font-size: 50px;
    color: gray;
    text-align: center;
}
.text{
    margin-top: 40px;
    font-size: 30px;
    color: gray;
    text-align: center;
}
.input_group{
    
    width: 100%;
    margin: 0 auto;
    margin-top: 80px;
    // background: rgb(117, 117, 117);
    .input_container{
        width: 32%;
        display: inline-block;
        .input_lable_tip{
            float: left;
            margin-right: 10px;
            font-size: 18px;
            color: rgb(255, 0, 0);
        }
        .input_lable_tip_gray{
            color: gray;
        }
        .input_lable_text{
            font-size: 18px;
            color: gray;
        }
    }
    .input_item{
        margin-top: 20px;
        width: 80%;
        height: 35px;
        font-size: 20px;
          -webkit-user-select:auto; /*webkit浏览器*/  
        user-select:auto;
        -o-user-select:auto;
        -ms-user-select:auto; 
        line-height: 35px;
    }
    .input_container_1{
        margin-top: 20px;
        width: 100%;

        .input_lable_tip{
            float: left;
            margin-right: 10px;
            font-size: 18px;
            color: rgb(255, 0, 0);
        }
        .input_lable_text{
            font-size: 18px;
            color: gray;
        }
        .textarea_item{
            width: 100%;
            margin-top: 20px;
            font-size: 16px;
            color: gray;
            height: 300px;
        }
    }
}
.center_cust_button{
    height: 35px;
    width: 250px;
    
    text-align: center;
    border:2px solid gray;
    line-height: 35px;
    font-size: 18px;
    color: gray;
    cursor:pointer;
    margin: 0 auto;
    margin-top: 60px;
    
    
}
.center_cust_button:hover{
    background: gray;
    color: white;
}
.abs_img_3{
    height: 220px;
    width: 253px;
    position: absolute;
    top: 100px;
    left: 150px;
    background:url("../assets/img_12.png") no-repeat center center;
}
.error_msg{
    margin-top: 30px;
    font-size: 16px;
    color: rgb(180, 0, 0);
    text-align: center;
    font-family: gillsans_light;
    letter-spacing: 1px;
}

</style>>
