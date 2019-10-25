<template>
<div id="content_header">

<div class="nav">
    <div class="logo">

    </div>

    <div class="nav_button_list">
        <div class="nav_button">
            <div class="nav_button_tip"></div>
            <div class="nav_button_contnet">Home</div>
        </div>
        <div class="nav_button">
            <div class="nav_button_tip"></div>
            <div class="nav_button_contnet">About</div>
        </div>
        <div class="nav_button">
            <div class="nav_button_tip"></div>
            <div class="nav_button_contnet">Programs
                <div class="drop_down_menu">
                    <div class="drop_down_menu_item"><a href="#">Curated Programs</a></div>
                    <div class="drop_down_menu_item"><a href="#">Programs China</a></div>
                    <div class="drop_down_menu_item"><a href="#">Curated China</a></div>
                </div>
            </div>
            
        </div>
        <div class="nav_button">
            <div class="nav_button_tip"></div>
            <div class="nav_button_contnet">Blogs</div>
        </div>
        <div class="nav_button">
            <div class="nav_button_tip"></div>
            <div class="nav_button_contnet">Contact</div>
        </div>
        <div class="nav_button">
            <div class="nav_button_tip_"></div>
            <div class="nav_button_contnet_">:</div>
        </div>
        <div class="nav_button">
            <div class="nav_button_tip_"></div>
            <div class="nav_button_contnet_">中文</div>
        </div>
        <div class="nav_button">
            <div class="nav_button_tip_"></div>
            <div class="nav_button_contnet_1">ENQUIRE</div>
        </div>
    </div>
</div>

<div class="content_1">
    <div class="title_list">
    <div class="title">Broaden your horizon</div>
    <div class="title">by a curated study tour in China</div>
    </div>
</div>

<div class="content_2">
    <div class="item_list">
        <div class="item">
            <div class="item_icon item_icon_0"></div>
            <div class="item_content">Education</div>
        </div>

        <div class="item">
            <div class="item_icon item_icon_1"></div>
            <div class="item_content">Insightful</div>
        </div>

        <div class="item">
            <div class="item_icon item_icon_2"></div>
            <div class="item_content">Dynamic</div>
        </div>
    </div>
    
</div>

<div class="content_3">
    
    <div class="button_item">Unlock Trips</div>
</div>

</div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.nav{
    .logo{
        background-image: url(../assets/logo.png);
        position: absolute;
        height: 100%;
        width: 100%;
        background-repeat:no-repeat;
        top: 5rem;
        left: 10rem;
    }

    .nav_button_list{
        position: absolute;
        right: 10rem;
        height: 10rem;
        display: flex;
        flex-direction: row;
        // background: gray;
        .nav_button{
            display: flex;
            flex-direction: column;
            justify-content:space-between;
            // background: rgba(94, 94, 94, 0.164);

            
            .nav_button_tip{
                height: 0.6rem;
                // background: red;
            }
            .nav_button_contnet{
                padding: 0.7rem 1.2rem 0.7rem 1.2rem;
                color: white;
                font-size: 1.7rem;
                // font-family:"font-family:Arial,Helvetica";
                font-weight:500;
            }
            .nav_button_contnet_{
                padding: 0.7rem 1.2rem 0.7rem 1.2rem;
                color: white;
                font-size: 1.7rem;
            }
            .nav_button_contnet_1{
                padding: 0.7rem 1.2rem 0.7rem 1.2rem;
                margin-left: 1rem;
                color: white;
                font-size: 1.7rem;
                background: rgb(172, 0, 0);
                // font-family:"font-family:Arial,Helvetica";
            }
            .drop_down_menu{
                margin-top: 0.5rem;
                display: none;
                position: absolute;
                background: rgba(128, 128, 128, 0.685);
                
                .drop_down_menu_item{
                    padding: 1.2rem 2.6rem;
                    a{
                        font-size: 1.7rem;
                        color: white;
                        // font-family:"font-family:Arial,Helvetica";
                    }
                }
                .drop_down_menu_item:hover{
                    background: rgb(255, 255, 255);
                    a{
                        color:rgb(74, 74, 74);
                        // font-family:"font-family:Arial,Helvetica";
                    }
                }
            }
        }
        .nav_button:hover{
            .nav_button_tip{
                background: rgb(219, 0, 0);
            }

            .nav_button_contnet{
                color: rgb(197, 197, 197);
                cursor:default;
                // background: rgba(114, 114, 114, 0.397);
            }
            .nav_button_contnet_{
                color: rgb(197, 197, 197);
                cursor:default;
            }
            .nav_button_contnet_1{
                background: rgb(141, 0, 0);
                cursor:default;
            }
            .drop_down_menu{
                display: block;
            }
        }
    }
}

#content_header{
    background-image: url(../assets/wall7.png);
    height: 80rem;
    background-position: top;
    background-size: cover;
    background-repeat:no-repeat;

    .content_1{
        width: 100%;
        top: 20rem;
        position: absolute;

        .title_list{
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            align-items: center;
            
            .title{
                color: white;
                font-size: 7rem;
                text-shadow: 0px 0px 10px black;
                
            }
        }
    }

    .content_2{

        position: absolute;
        width: 100%;
        top: 43rem;
        .item_list{
            display: flex;
            justify-content: center;
            flex-direction: row;
            .item{

                .item_icon_0{
                    background-image: url(../assets/edu.png);
                    height: 100%;
                    width: 100%;
                    background-repeat:no-repeat;
                    filter: hue-rotate(180deg);
                }
                .item_icon_1{
                    background-image: url(../assets/ins.png);
                    height: 100%;
                    width: 100%;
                    background-repeat:no-repeat;
                }
                .item_icon_2{
                    background-image: url(../assets/dyn.png);
                    height: 100%;
                    width: 100%;
                    background-repeat:no-repeat;
                }
                .item_content{
                    color: white;
                    text-align: center;
                    font-size: 2.5rem;
                }
                height: 8rem;
                width: 8rem;
                margin: 0rem 4rem 0rem 4rem;
                // background: red;
                
            }
        }
        
    }

    .content_3{
        position: absolute;
        width: 100%;
        top: 63rem;
        display: flex;
        justify-content: center;
        flex-direction: row;
        .button_item{
            // background: red;
            border: 0.25rem solid white;
            padding: 1rem;
            font-size: 2.5rem;
            color: white;
        }
        .button_item:hover{
            background: white;
            color: rgb(74, 74, 74);
        }

    }
}
</style>>
