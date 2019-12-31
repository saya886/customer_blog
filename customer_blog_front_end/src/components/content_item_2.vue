<template>
<div class="main">
    <div class="header_content">We diversify and enrich your learning experiences in China <br>
with the following four valuable building blocks.</div>
    <div class="item_group">
        <div class="item_row">
            <div class="item item_left">
                <div class="item_d1 item_content_1">
                <div class="img_abs"><img class="inline_img" src="../assets/img_39.png"><span class="index_count">I :</span></div>
                Theoretical</div> 
            </div>
            <div class="item item_mid">
                <div class="item_d2 item_content_2">Sitting in the classroom of China’s top <br>
universities and absorbing the <br>
knowledge from prestigious professors.</div>
                <div class="item_move item_move_right">
                    <div class="item_content_3 item_content_img_1"></div>
                </div>
            </div>
            <div class="item item_right">
            </div>
        </div>

        <div class="item_row">
            <div class="item item_left">
                
            </div>
            <div class="item item_mid">
                <div class="item_d1 item_content_1">
                <div class="img_abs_1"><img class="inline_img" src="../assets/img_39.png"><span class="index_count">Ⅱ:</span></div>
                Practical</div>
                <div class="item_move item_move_left">
                    <div class="item_content_3 item_content_img_2"></div> 
                </div>
            </div>
            <div class="item item_right">
                <div class="item_content_2 item_d2">Visiting the leading enterprises and <br>
attending workshops to interact <br>with the entrepreneurs that have rich <br>hands-on experiences in Chinese market</div>
            </div>
        </div>

        <div class="item_row">
            <div class="item item_left">
                <div class="item_d1 item_content_1"><div class="img_abs_2"><img class="inline_img" src="../assets/img_39.png"><span class="index_count">Ⅲ:</span></div>
                Cultural</div> 
            </div>
            <div class="item item_mid">
                <div class="item_d2 item_content_2">Learning the essence of various Chinese<br>traditional culture by talking to <br>the 
Chinese artisans or craftsmen and <br>
exploring the historical sites.</div>
                <div class="item_move item_move_right">
                    <div class="item_content_3 item_content_img_3"></div>
                </div>
            </div>
            <div class="item item_right">
            </div>
        </div>

        <div class="item_row">
            <div class="item item_left">
                
            </div>
            <div class="item item_mid">
                <div class="item_d1 item_content_1">
                <div class="img_abs_2"><img class="inline_img" src="../assets/img_39.png"><span class="index_count">Ⅳ:</span></div>Entrepreneurial</div>
                <div class="item_move item_move_left">
                    <div class="item_content_3 item_content_img_4"></div> 
                </div>
            </div>
            <div class="item item_right">
                <div class="item_content_2 item_d2">Getting valuable career development suggestions; Help facilitating or launching business projects in Chinese market.</div>
            </div>
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
    background: rgba(233, 229, 229, 0.445);
    height: 2150px;
}
.header_content{
    padding-top:134px;
    padding-bottom:100px;
    text-align: center;
    font-size: 30px;
    color: gray;
    line-height: 50px;
}
.item_group{
    // background: gray;
    // height: 1500px;
    width: 1200px;
    margin: 0 auto;
}
.item_row{
    height: 400px;
    // background: red;
    display: flex;
    flex-direction: row;
    .item{
        width: 400px;
        // background: blue;
        height: 100%;
        // display: inline-block;
    }
    .item_left{
        .item_d2{
            background: #3F3F3F;
            height: 400px;
            width: 400px;
        }
        .item_d1{
            background: #333333; 
            height: 400px;
            width: 400px;
            position:relative;   
        }
    }
    .item_right{
        .item_d2{
            background: #3F3F3F;
            height: 400px;
            width: 400px;
        }
        .item_d1{
            background: #333333; 
            height: 400px;
            width: 400px;
            // position:relative;   
        }
    }
    .item_mid{
        position: relative;
        .item_d2{
            position: absolute;
            background: #3F3F3F;
            height: 400px;
            width: 400px;
            z-index: 2;
            // display: none;
            // top: -400px;
        }
        .item_d1{
            position: absolute;
            background: #333333;
            height: 400px;
            width: 400px;
            z-index: 2;
            // position:relative;
            // display: none;
            // top: -400px;
        }
        .item_move{
            background: rgb(255, 255, 255);
            position: absolute;
            height: 400px;
            width: 400px;
            z-index: 1;
            transition-duration: 0.6s;
            transition-timing-function: cubic-bezier(0.165, 0.84, 0.44, 1);
            
        }
    }
    
    .item_mid:hover{
        .item_move_right{
            transform:translateX(400px);
        }
        .item_move_left{
            transform:translateX(-400px);
        }
    }
    .item_move_left{
        background: rgb(255, 255, 255);
    }
}
.item_content_1{
    
    font-size: 50px;
    color: rgb(241, 241, 241);
    display: flex;
    flex-direction: row;
    align-items:center;
    justify-content:center;
}
.item_content_2{
    font-size: 18px;
    color: rgb(241, 241, 241);
    display: flex;
    flex-direction: row;
    align-items:center;
    justify-content:center;
    text-align: center;
    line-height:25px;
}
.item_content_3{
    height: 400px;
    width: 400px;
}

.item_content_img_1{
    background:url("../assets/img_13.png") no-repeat center;
}
.item_content_img_2{
    background:url("../assets/img_14.png") no-repeat center;
}
.item_content_img_3{
    background:url("../assets/img_15.png") no-repeat center;
}
.item_content_img_4{
    background:url("../assets/img_16.png") no-repeat center;
}

.img_abs{
    position:absolute;
    top:120px;
    left:80px;
}
.img_abs_1{
    position:absolute;
    top:120px;
    left:110px;
}
.img_abs_2{
    position:absolute;
    top:120px;
    left:190px;
}
.inline_img{
    display:inline;
}
.index_count{
    font-size:15px;
    margin-left:10px;
}
</style>>
