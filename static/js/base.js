
/* eslint-disable */

/**
 * 获取url参数值（query）
 * */
function getUrlParam(name) {
    var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)');
    var url = window.location.search.substr(1).match(reg);
    if (url !== null) {
        return decodeURIComponent(url[2]);
    }
    return null;
}

// 增加月数
function addMonth(date, months) {
    var startTime = date ? date : new Date();
    if (startTime < new Date()) {
        startTime = new Date();
        startTime.setDate(startTime.getDate() + 1);
    }
    startTime.setHours(0, 0, 0, 0);
    startTime.setMonth(startTime.getMonth() + months);
    return startTime;
}

/**
 * 添加天数
 */
function addDays(date, days) {
    var startTime = date || new Date();
    if (startTime < new Date()) {
        startTime = new Date();
    }
    var newTime = startTime.getTime() + (days * 24 * 60 * 60 * 1000);
    return new Date(newTime);
}

/**
 * 获取两个时间之间的天数
 */
function dateDiffDays(startDate, endDate) {
    var dateSpan = Math.abs(Date.parse(endDate) - Date.parse(startDate));
    return Math.floor(dateSpan / (24 * 3600 * 1000));
}

/**
 * 获取cookie参数值（query）
 * */
function getCookie(name) {
    var arr;
    var reg = new RegExp('(^| )' + name + '=([^;]*)(;|$)');
    if ((arr = document.cookie.match(reg))) {
        return unescape(arr[2]);
    } else {
        return null;
    }
}

/**
 * 判断是否是微信浏览器打开
 * */
function isWeiXin() {
    var ua = window.navigator.userAgent.toLowerCase();
    return ua.match(/MicroMessenger/i) === 'micromessenger';
}

/**
 * 判断是否是移动端
 * */
function isH5() {
    return /(iPhone|iPad|iPod|iOS|Android)/i.test(navigator.userAgent);
}

/**
 * 格式化日期（不含时间）
 */
function formatterDate(date) {
    var newDate = new Date(date);
    var datetime =
        newDate.getFullYear() +
        '-' +
        (newDate.getMonth() + 1 > 10 ? newDate.getMonth() + 1 : '0' + (newDate.getMonth() + 1)) +
        '-' +
        (newDate.getDate() < 10 ? '0' + newDate.getDate() : newDate.getDate());
    return datetime;
}

/**
 * 显示错误提示
 * */
function showMessage(message) {
    var $msg = $(
        '<div class="msg-box">' +
        '<img class="warning" src="/images/icon/error.png" width="20"/>' +
        '<p>' +
        message +
        '</p>' +
        '</div>');
    $msg.appendTo(document.body);
    setTimeout(function () {
        $msg.remove();
    }, 2e3);
}

/**
 * 显示成功提示
 * */
function showSuccess(message) {
    var $msg = $(
        '<div class="msg-box">' +
        '<img class="success" src="/images/icon/success.png" width="20"/>' +
        '<p>' +
        message +
        '</p>' +
        '</div>');
    $msg.appendTo(document.body);
    setTimeout(function () {
        $msg.remove();
    }, 2e3);
}

/**
 * 显示成功提示
 * @message 显示提示的信息
 * @ok 确认按钮值，为空值则不显示该按钮
 * @cancel 取消按钮值，为空值则不显示该按钮
 * */
function showConfig(message, ok, cancel) {
    var $msg = $(
        '<div class="msg-box">' +
        '<i id="icon" class="iconfont icon_demo_close"></i>' +
        '<p>' +
        message +
        '</p>' +
        '<div class="btn"><span id="ok">' +
        ok +
        '</span>' +
        '<span id="cancel">' +
        cancel +
        '</span></div>' +
        '</div>');
    $msg.appendTo(document.body);
    $('#ok, #cancel, #icon').click(function () {
        $('input').val('');
        $('textarea').val('');
        $msg.remove();
    });
}

function validEmail(email) {
    var reg = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return reg.test(email);
}

function verifyPhone(tel) {
    var reg = /^(1\d{10})$/;
    return reg.test(tel);
}

function checkUrl(url) {
    var reg = /(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?/;
    return reg.test(url);
}

/**
 * 验证密码
 * */
function verifyPwd(pwd) {
    var reg = /^\S{6,20}$/;
    return reg.test(pwd);
}

/**
 * 轮播方法
 * */
function banner(parent, img, active, li) {
    var index = 0;
    var len = $(img).length - 1;
    var fl;
    var winHeight = $(window).height();
    var itemOffsetTop = $(parent).offset().top;

    function teb(idx) {
        $(li).eq(idx).addClass(active).siblings('').removeClass(active);
        $(img).eq(idx).addClass('active').siblings('').removeClass('active');
    }

    $(li).hover(function () {
        index = $(this).index();
        teb(index);
        clearInterval(fl);
        timeRun();
    });

    $(li).click(function () {
        index = $(this).index();
        teb(index);
        clearInterval(fl);
        timeRun();
    });

    function timeRun() {
        fl = setInterval(function () {
            index++;
            if (index > len) {
                index = 0;
            }
            teb(index);
        }, 5e3);
    }

    // 判断元素是否在可视区域内，是否需要启动自动轮播
    function isVisible() {
        var winScrollHeight = $(window).scrollTop();
        clearInterval(fl);
        if (winScrollHeight + winHeight > itemOffsetTop && winScrollHeight < itemOffsetTop + winHeight) {
            timeRun();
        }
    }

    isVisible();
    $(window).scroll(function () {
        isVisible();
    });
}

/**
 * 顶部导航控制
 * */
var $userInfo = $('#userInfo');
var $userSubMenu = $('#userInfo .user-menu');
var $wx = $('.wx-box');
var $navSpan = $('.nav-menu .nav-item > span');
var $navItem = $('.nav-menu .nav-item');
var $header = $('.header-of-page');
var $phMenuIcon = $('.ph-menu-icon');
var $phMenuClose = $('.ph-head .ph-menu-icon');

/**
 * 下拉导航
 **/
$navSpan.click(function () {
    var windowWidth = window.innerWidth;
    if (windowWidth > 999) {
        $userSubMenu.hide();
        if ($(this).parents('.nav-item').hasClass('active')) {
            $(this).parents('.nav-item').removeClass('active');
            $(this).parents('.nav-item').find('.nav-menu-drop').css('display', 'none');
            $header.removeClass('active');
        } else {
            $navItem.removeClass('active');
            $('.nav-menu-drop').css('display', 'none');
            $(this).parents('.nav-item').addClass('active');
            $(this).parents('.nav-item').find('.nav-menu-drop').css('display', 'block');
            $header.addClass('active');
        }
    } else {
        $(this).find('.iconfont').addClass('icon_broad_back');
        $(this).find('.iconfont').removeClass('icon_broad_pre-copy');
        if ($(this).parents('.nav-item').find('.nav-menu-drop').css('display') === 'block') {
            $(this).parents('.nav-item').find('.nav-menu-drop').slideUp(200);
        } else {
            $navItem.find('.nav-menu-drop').slideUp(200);
            $(this).parents('.nav-item').find('.nav-menu-drop').slideDown(200);
            $(this).find('.iconfont').removeClass('icon_broad_back');
            $(this).find('.iconfont').addClass('icon_broad_pre-copy');
        }
    }
});

/**
 * 头像下拉
 * */
$userInfo.click(function (e) {
    closeHeaderSubMenu();
    if ($('.message-pops').css('display') === 'block') {
        $('.message-pops').hide();
    }
    if ($userSubMenu.css('display') === 'none') {
        $userSubMenu.show();
    } else {
        $userSubMenu.hide();
    }
    e.stopPropagation();
});

function closeHeaderSubMenu() {
    $('body').css('position', 'static');
    $('.nav-menu-drop').css('display', 'none');
    $navItem.removeClass('active');
    $('.header-of-page').removeClass('active');
}

/**
 * 小屏幕菜单出现与隐藏
 * */
$phMenuIcon.click(function () {
    $header.addClass('active');
    $('body').css('position', 'fixed');
});

$phMenuClose.click(function () {
    closeHeaderSubMenu();
});

$(window).resize(function () {
    var windowWidth = window.innerWidth;
    if (windowWidth <= 999 && $header.hasClass('active')) {
        $('body').css('position', 'fixed');
    } else {
        $('body').css('position', 'static');
    }

    if (windowWidth > 999) {
        $('.nav-menu-drop').each(function () {
            if ($(this).parents('.nav-item').hasClass('active')) {
                $(this).css('display', 'block');
            } else {
                $(this).css('display', 'none');
            }
        });
    }
});

$('body').click(function (e) {
    var windowWidth = window.innerWidth;
    // 点击空白处收起下拉导航
    if (
        windowWidth > 999 &&
        !$navItem.is(event.target) &&
        $navItem.has(event.target).length === 0 &&
        !$phMenuIcon.is(event.target) &&
        $phMenuIcon.has(event.target).length === 0 &&
        !$header.is(event.target) &&
        $header.has(event.target).length === 0
    ) {
        closeHeaderSubMenu();
    }
    // 点击空白处收起个人中心下拉
    if (windowWidth > 999 && !$navItem.is(event.target) && $navItem.has(event.target).length === 0) {
        $userSubMenu.hide();
    }
});

/**
 * 小屏头部微信出现与收起
 */
$wx.click(function () {
    if ($(this).hasClass('active')) {
        $(this).removeClass('active');
    } else {
        $(this).addClass('active');
    }
});

/**
 * 小屏底部下拉与收起
 */
$('.footer-phone .footer-content .footer-item h3').click(function () {
    var thisParents = $(this).parents('.footer-item');
    if (thisParents.hasClass('active')) {
        thisParents.removeClass('active');
        thisParents.find('ul').slideUp(200);
    } else {
        thisParents.addClass('active');
        thisParents.find('ul').slideDown(200);
    }
});

/**
 * 小屏底部导航栏控制
 * */
var $firm = $('#firm');
var $firmList = $('#firm-list');
var $browse = $('#browse');
var $browseList = $('#browse-list');
var $support = $('#support');
var $supportList = $('#support-list');
var $about = $('#about');
var $aboutList = $('#about-list');

/**
 * 小屏企业版下拉
 * */
// $firm.click(function (e) {
//   if ($firmList.css('display') === 'none') {
//     $firmList.show();
//     $firm.find('.iconfont').addClass('icon_broad_back');
//     $firm.find('.iconfont').removeClass('icon_Right');
//   } else {
//     $firmList.hide();
//     $firm.find('.iconfont').addClass('icon_Right');
//     $firm.find('.iconfont').removeClass('icon_broad_back');
//   }
//   e.stopPropagation();
// });

/**
 * 小屏浏览下拉
 * */
// $browse.click(function (e) {
//   if ($browseList.css('display') === 'none') {
//     $browseList.show();
//     $browse.find('.iconfont').addClass('icon_broad_back');
//     $browse.find('.iconfont').removeClass('icon_Right');
//   } else {
//     $browseList.hide();
//     $browse.find('.iconfont').addClass('icon_Right');
//     $browse.find('.iconfont').removeClass('icon_broad_back');
//   }
//   e.stopPropagation();
// });

/**
 * 小屏支持下拉
 * */
// $support.click(function (e) {
//   if ($supportList.css('display') === 'none') {
//     $supportList.show();
//     $support.find('.iconfont').addClass('icon_broad_back');
//     $support.find('.iconfont').removeClass('icon_Right');
//   } else {
//     $supportList.hide();
//     $support.find('.iconfont').addClass('icon_Right');
//     $support.find('.iconfont').removeClass('icon_broad_back');
//   }
//   e.stopPropagation();
// });

/**
 * 小屏关于下拉
 * */
// $about.click(function (e) {
//   if ($aboutList.css('display') === 'none') {
//     $aboutList.show();
//     $about.find('.iconfont').addClass('icon_broad_back');
//     $about.find('.iconfont').removeClass('icon_Right');
//   } else {
//     $aboutList.hide();
//     $about.find('.iconfont').addClass('icon_Right');
//     $about.find('.iconfont').removeClass('icon_broad_back');
//   }
//   e.stopPropagation();
// });

$('.close').click(function (e) {
    closeHeaderSubMenu();
    e.stopPropagation();
});

/**
 * 雪碧图logo背景位置
 * x:初始x坐标 y:y坐标增量 m:li数量
 * */
function spritesBg(x, y, m) {
    for (var n = 0; n < m; n++) {
        $('#spriteslogo').append("<li class='sprites'></li>");
    }

    for (var i = 0; i < 100; i++) {
        for (var j = 0; j < i; j++) {
            var sum = -x;
            sum += -i * y;
        }
        $('#spriteslogo > li').eq(i).css({ backgroundPositionY: sum });
    }
}

// 固定博客页header-bg
var $headerOfPage = $('.header-of-page');
function fixedHeaderBg() {
    var winWidth = $(window).width();
    var $head = $('.header-content');
    var top = $(window).scrollTop();
    if (winWidth > 999) {
        if (top >= 1) {
            $headerOfPage.addClass('bg-color').css({ boxShadow: 'rgb(220, 220, 220) 0 2px 10px' });
            $('.en-link').css({ color: '#5C5758' });
            $head.removeClass('black-bg');
        } else {
            $headerOfPage.removeClass('bg-color').css({ boxShadow: 'none' });
            $head.addClass('black-bg');
            $('.en-link').css({ color: '#fff' });
        }
    } else {
        if (top >= 1) {
            $headerOfPage.addClass('bg-color').css({ boxShadow: 'rgb(220, 220, 220) 0 2px 10px' });
            $head.removeClass('black-bg');
        } else {
            $headerOfPage.removeClass('bg-color').css({ boxShadow: 'none' });
            $head.addClass('black-bg');
        }
    }
}

//博客有AD时固定header
function adHeader() {
    var top = $(window).scrollTop();
    var $ad = $('#banner-mp-ad');
    if ($ad.css('display') === 'block') {
        if (top >= 1) {
            $headerOfPage.css({ top: $ad.innerHeight(), boxShadow: 'rgb(220, 220, 220) 0 2px 10px' });
        } else {
            $headerOfPage.css({ top: $ad.innerHeight(), boxShadow: 'none' });
        }
    } else {
        $headerOfPage.css({ top: 0 });
    }
}

// //懒加载
// var n = 0;
// var imgNum = $('img').length;
// var img = $('img');
// lazyload();

// $(window).scroll(function () {
//     lazyload();
// });

// function lazyload() {
//     var winHeight = $(window).height();
//     var winTop = $(window).scrollTop();
//     for (var i = 0; i < imgNum; i++) {
//         if (img.eq(i).offset().top < parseInt(winHeight) + parseInt(winTop)) {
//             if (img.eq(i).attr('src') === 'default.png') {
//                 var src = img.eq(i).attr('data-src');
//                 img.eq(i).attr('src', src);
//                 n = i + 1;
//             }
//         }
//     }
// }

//禁止滚动条滚动
function unScroll() {
    var top = $(document).scrollTop();
    $(document).on('scroll.unable', function () {
        $(document).scrollTop(top);
    });
}

//移除禁止滚动条滚动
function removeUnScroll() {
    $(document).unbind('scroll.unable');
}

//  飞书屏蔽默认header
if (window.navigator.userAgent.indexOf('LarkLocale') !== -1) {
    $('.header-content').hide();
    $('.header-lark').show();
    $('#banner-mp-ad').css('top', '37px');
}

//添加插件下载日志
$('.idoc-plugin-download-log').click(function () {
    var ua = window.navigator.userAgent.toLowerCase();
    var downloadURL = $(this).attr('href');
    $.post('/download/addDownloadLog', {
        ua: ua,
        downloadURL: downloadURL,
        product: 'idoc'
    }, function (res) {
        console.log(res);
    });
});

//添加mockplus下载日志
$('.mockplus-download-log').click(function () {
    var ua = window.navigator.userAgent.toLowerCase();
    var downloadURL = $(this).attr('href');
    $.post('/download/addDownloadLog', {
        ua: ua,
        downloadURL: downloadURL,
        product: 'mockplus'
    }, function (res) {
        console.log(res);
    });
});

//添加mockplus-rp下载日志
$('.mockplus-rp-download-log').click(function () {
    var ua = window.navigator.userAgent.toLowerCase();
    var downloadURL = $(this).attr('href');
    $.post('/download/addDownloadLog', {
        ua: ua,
        downloadURL: downloadURL,
        product: 'rp'
    }, function (res) {
        console.log(res);
    });
});

/**
 * 新年视频弹出与消失
 * */
var myPlayerNewYear = $('.global-video-bullet-box-new-year #my-video-new-year');
$('.play-video-new-year').click(function () {
    $('.global-video-bullet-box-new-year').fadeIn(500);
    videojs('my-video-new-year').ready(function () {
        var myPlayerNewYear = this;
        myPlayerNewYear.play();
    });
    myPlayerNewYear.show();
    $('html').css({ height: '100%', overflow: 'hidden' });
});

$('.video-cancel-new-year').click(function () {
    console.log(1111);
    $('.global-video-bullet-box-new-year').fadeOut(100);
    myPlayerNewYear.hide();
    videojs('my-video-new-year').load();
    $('html').css({ height: 'auto', overflow: 'auto' });
});
