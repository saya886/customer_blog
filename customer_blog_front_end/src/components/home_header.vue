<template>
<div class="main">
    <div class="header">
        <div class="logo"></div>
        <div class="menu">

            <div class="nva_item">
                <div class="nav_tip"></div>
                <div class="nav_link">Home</div>
                <div class="nav_drop_down">
                    <div class="nav_drop_down_item">
                        <a href="#">你好</a>
                    </div>
                </div>
            </div>

            <div class="nva_item">
                <div class="nav_tip"></div>
                <div class="nav_link">About</div>
                <div class="nav_drop_down">
                    <div class="nav_drop_down_item">
                        <a href="#">你好</a>
                    </div>
                </div>
            </div>

            <div class="nva_item">
                <div class="nav_tip"></div>
                <div class="nav_link">Programs</div>
                <div class="nav_drop_down">
                    <div class="nav_drop_down_item">
                        <a href="#">Curated Programs</a>
                    </div>
                    <div class="nav_drop_down_item">
                        <a href="#">Programs China</a>
                    </div>
                    <div class="nav_drop_down_item">
                        <a href="#">CuratedChina</a>
                    </div>
                </div>
            </div>

            <div class="nva_item">
                <div class="nav_tip"></div>
                <div class="nav_link">Blogs</div>
                <div class="nav_drop_down">
                    <div class="nav_drop_down_item">
                        <a href="#">你好</a>
                    </div>
                </div>
            </div>

            <div class="nva_item">
                <div class="nav_tip"></div>
                <div class="nav_link">Contact</div>
                <div class="nav_drop_down">
                    <div class="nav_drop_down_item">
                        <a href="#">你好</a>
                    </div>
                </div>
            </div>

            <div class="nva_item nav_divider">
                <div class="nav_link">:</div>
            </div>

            <div class="nva_item">
                <div class="nav_link">中文</div>
            </div>

            <div class="nva_item nva_buttom">
                <div class="nav_link">ENQUIRE</div>
            </div>

        </div>
    </div>
    <div class="content_1">
        <div class="title_1 title">Broaden your horizon</div>
        <div class="title">by a curated study tour in China</div>
        <div class="divider"></div>
        <div class="icon_group">
            <div class="icon_ietm">
                <div class="icon_image icon_image_edu"></div>
                <div class="icon_content">
                    Educational
                </div>
            </div>
            <div class="icon_ietm">
                <div class="icon_image icon_image_ins"></div>
                <div class="icon_content">
                    Insightful
                </div>
            </div>
            <div class="icon_ietm">
                <div class="icon_image icon_image_dyn"></div>
                <div class="icon_content">
                    Dynamic
                </div>
            </div>
        </div>
        <div class="center_button">Unlock Trips</div>
    </div>
</div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.main{
    height: 899px;
    
    background:url("../assets/home_header_dark.png") no-repeat center center;
    background-size: cover;
}

.header{
    height: 100px;
    // background: rgba(255, 0, 0, 0.445);
}
.logo{
    background: red;
    height: 100%;
    width: 230px;
    float: left;
    margin-left: 120px; 
    background:url("../assets/logo.png") no-repeat center center;
}
.menu{
    // background: red;
    width: 930px;
    height: 100%;
    float: right;   
}

.title{
    // background: red;
    
    margin: 0 auto;
    margin-top: 10px;
    width: 1000px;  
    height: 70px;
    font-size: 70px;
    color: white;
    text-align: center;
    text-shadow: 5px 5px 8px #000000;
}
.title_1{
    margin-top:130px; 
}
.divider{
    background: red;
    
    margin: 0 auto;
    margin-top: 60px;
    margin-bottom: 60px;
    width: 1211px;  
    height: 15px;
    background:url("../assets/divider_1_white.png") no-repeat center center;
}
.icon_group{
    // background: red;
    
    margin: 0 auto;
    margin-top: 20px;
    width: 550px;  
    height: 130px;
    // padding: 5px;
    .icon_ietm{
        display: inline-block;
        // background: green;
        width: 32%;
        height: 100%;
        padding: 2px;
        .icon_image{
            // background: red;
            height: 100px;
            
        }
        .icon_image_edu{
            background:url("../assets/edu.png") no-repeat center;
        }
        .icon_image_ins{
            background:url("../assets/ins.png") no-repeat center;
        }
        .icon_image_dyn{
            background:url("../assets/dyn.png") no-repeat center;
        }
        .icon_content{
            text-align: center;
            color: white;
            font-size: 23px;
            line-height: 24px;
        }

    }
}
.center_button{
    height: 45px;
    width: 160px;
    margin: 0 auto;
    margin-top: 70px; 
    
    text-align: center;
    border:4px solid white;
    line-height: 45px;
    font-size: 23px;
    color: white;
    cursor:pointer;
    
}
.center_button:hover{
    background: white;
    color: black;
}
.nva_item{
    position: relative;
    // background: green;
    width: 11%;
    height: 100%;
    margin-right:10px;
    display: inline-block;
    .nav_tip{
        position: absolute;
        // background: red;
        height: 5px;
        width: 100%;
    }
    .nav_link{
        text-align: center;
        position: absolute;
        bottom: 10px;
        width: 100%;
        color: white;
        font-size: 20px;

    }
    .nav_link:hover{
        cursor:pointer;
    }
    .nav_drop_down{
        margin-top: 100px;
        display: none;
        position: absolute;
        background: rgba(92, 92, 92, 0.404);
        
        width: 200px;
        .nav_drop_down_item{
            padding: 10px 20px 10px 20px;
        }
        .nav_drop_down_item:hover{
            cursor:pointer;
            background: white;
            a{
                color: black;
            }
            
        }
        a{
            color: white;
            font-size: 20px;
        }
    }
}
.nva_item:hover{
    .nav_drop_down{
        display: block;
    }
    .nav_tip{
        background: red;
    }
}
.nav_divider{
    width: 20px;
    .nav_link:hover{
        cursor:default;
    }
}
.nva_buttom{
    .nav_link{
        background: red;
        line-height: 30px;
        height: 30px;
    }
}
</style>>
