<template>
<div class="main">
    <div class="item">
        <div class="title">Testimonials</div>
        <div class="divider"></div>
        <div class="text_item">{{c_item.message}}</div>
        <div class="icon_group">
            <div class="icon_ietm">
                
                <img class="icon_image" v-bind:src="c_item.img_src" alt="">
                <div class="icon_content">
                    {{c_item.content}}
                </div>

                
            </div>
            <img @click="click_last()" class="last control_button" src="../assets/left.png" alt="">
            <img @click="click_next()" class="next control_button" src="../assets/right.png" alt="">
        </div>

        
    </div>
</div>
</template>

<script>
export default {
    data(){
        return{
            "is_show":true,
            "index":0,
            "data_list":[

            ]
        }
    },
    mounted (){
        this.$axios({
            method: "get",
            url: "/testimonials",
        }).then(response => {
            console.log(response, "success");   // 成功的返回
            this.data_list = response["data"]["data"]
        })
        .catch(error => {
            console.log(error, "error")
        }); // 失败的返回
    },
    methods:{
        go_to_detail(program_id){
            console.log(program_id);
            this.$router.push("/programs/"+program_id.toString())
        },
        click_next(){
            this.index = this.index + 1
        },
        click_last(){
            this.index = this.index - 1
        }
        
    },
    computed:{
        c_item(){
            if(this.data_list.length > 0){
                if(this.index <= this.data_list.length-1){
                    if(this.index >= 0){
                        return this.data_list[this.index]
                    }else{
                        this.index = 0
                        return this.data_list[0]
                    }
                    
                }else{
                    this.index = 0
                    return this.data_list[0]
                }
            }else{
                return {
                    "content":"",
                    "img_src":"",
                    "content":""
                }
            }
        }
    }
}
</script>

<style lang="less" scoped>
.main{
    // background: rgba(255, 0, 0, 0.445);
    height: 700px;
    padding: 120px 140px 120px 140px;
}
.item{
    // background: rgba(0, 0, 255, 0.384);
    height: 100%;
    border:3px solid rgb(136, 136, 136);
    // padding: 80px;  
    
    
}
.title{
    margin-top: 40px;
    text-align: center;
    color: rgb(82, 82, 82);
    font-size: 36px;
}
.divider{
    // background: green;
    
    margin: 0 auto;
    margin-top: 30px;
    margin-bottom: 40px;
    width: 100%;  
    height: 15px;
    background:url("../assets/divider_1_black.png") no-repeat center center;
}
.text_item{
    text-align: center;
    color: rgb(82, 82, 82);;
    font-size: 24px;
    line-height: 45px;
    width: 650px;
    margin: 0 auto;
}
.icon_group{
    margin-top: 60px;
    width: 100%;  
    // height: 50px;
    position: relative;
    // padding: 5px;
    .icon_ietm{
        // display: inline-block;
        // background: green;
        width: 32.8%;
        margin:0 auto;
        height: 50px;
        padding: 2px;
        
        .icon_image{
            // background: red;
            height: 214px;
            // opacity:0.4;
            
        }
        .icon_image_edu{
            background:url("../assets/img_6.png") no-repeat center;
        }
        .icon_image_ins{
            background:url("../assets/img_6.png") no-repeat center;
        }
        .icon_image_dyn{
            background:url("../assets/img_6.png") no-repeat center;
        }
        // .icon_image:hover{
        //     opacity:1;
        // }
        .icon_content{
            margin-top: 40px; 
            text-align: center;
            color: rgb(82, 82, 82);;
            font-size: 12px;
            line-height: 24px;
        }

    }
    
}
.control_button{
    height:40px;
    width:40px;
    position: absolute;
}
.control_button:hover{
    transform: scale(1.3,1.3);
    cursor: pointer;
    // box-shadow: 0px 0px 2px 2px gray;
}
.last{
    left:250px;
}
.next{
    right:250px;
}
</style>>
