(function () {
   const contentWayPoint = function () {
      let i = 0;

      $('.animate-box').waypoint(function (direction) {
         if (direction === 'down' && !$(this.element).hasClass('animated-fast')) {
            i++;

            $(this.element).addClass('item-animate');
            setTimeout(function () {

               $('body .animate-box.item-animate').each(function (k) {
                  const el = $(this);
                  setTimeout(function () {
                     const effect = el.data('animate-effect');

                     if (effect === 'fadeIn') {
                        el.addClass('fadeIn animated-fast');
                     } else if (effect === 'fadeInLeft') {
                        el.addClass('fadeInLeft animated-fast');
                     } else if (effect === 'fadeInRight') {
                        el.addClass('fadeInRight animated-fast');
                     } else {
                        el.addClass('fadeInUp animated-fast');
                     }

                     el.removeClass('item-animate');
                  }, k * 200, 'easeInOutExpo');
               });
            }, 100);
         }
      }, {
         offset: '85%'
      });
   };

   const goToTop = function () {
      $('.js-gotop').on('click', function (event) {
         event.preventDefault();

         $('html, body').animate({
            scrollTop: $('html').offset().top
         }, 1500, 'easeInOutExpo');

         return false;
      });

      $(window).scroll(function () {
         const $win = $(window);

         if ($win.scrollTop() > 200) {
            $('.js-top').addClass('active');
         } else {
            $('.js-top').removeClass('active');
         }
      });
   };

   // Loading page
   const loaderPage = function () {
      $(".fh5co-loader").fadeOut("slow");
   };

   const counter = function () {
      $('.js-counter').countTo({
         formatter: function (value, options) {
            return value.toFixed(options.decimals);
         },
      });
   };

   const counterWayPoint = function () {
      if ($('#fh5co-counter').length > 0) {
         $('#fh5co-counter').waypoint(function (direction) {

            if (direction === 'down' && !$(this.element).hasClass('animated')) {
               setTimeout(counter, 400);
               $(this.element).addClass('animated');
            }
         }, {
            offset: '90%'
         });
      }
   };

   $('.dropdown').click(function () {
      $(this).attr('tabindex', 1).focus();
      $(this).toggleClass('active');
      $(this).find('.dropdown-menu').slideToggle(300);
   });
   $('.dropdown .dropdown-menu li').click(function (e) {
      e.stopPropagation();
      $(this).parents('.dropdown').find('span').text($(this).text());
      $(this).parents('.dropdown').find('input').attr('value', $(this).attr('id'));
   });

   $('#it-3-btn').click(function () {
      const question = $('.it-3-question');
      const answer = $('.it-3-visibility');
      const counter = $('.it-3-timer');
      const duration = 800;
      let str = 60;

      counter.html(str + ' сек');

      $(this).prop('disabled', 'true');

      question.fadeIn(duration);
      counter.fadeIn(duration);

      const timer = setInterval(() => counter.html((str--) - 1 + ' сек'), 1000);

      setTimeout(() => {
         clearInterval(timer);
         answer.fadeIn(duration);
         question.hide();
         counter.hide();
      }, 60000)
   });

   $('#it-2-btn').click(function() {
      const textArea = $('#test-2-textarea');
      const testItem1 = $('.test_2_item-1');
      const counter = $('.it-2-timer');
      const duration = 800;
      let str = 45;
      $(this).prop('disabled', 'true');
      counter.html(str + ' сек');
      testItem1.fadeIn();
      counter.fadeIn(duration);
      

      const timer = setInterval(() => counter.html((str--) - 1 + ' сек'), 1000);

      setTimeout(() => {
         clearInterval(timer);
         textArea.fadeIn(duration);
         testItem1.hide();
         counter.hide();
      }, 45000)

      setTimeout(() => {
         textArea.hide(duration);
         $(this).hide();
         $('#it-2-btn-2').show();
      }, 90000)
   })

   $('#it-2-btn-2').click(function() {
      const textArea = $('#test-2-textarea');
      const testItem1 = $('.test_2_item-2');
      const counter = $('.it-2-timer');
      const duration = 800;
      let str = 45;
      $(this).prop('disabled', 'true');

      counter.html(str + ' сек');
      testItem1.fadeIn();
      counter.fadeIn(duration);

      const timer = setInterval(() => counter.html((str--) - 1 + ' сек'), 1000);

      setTimeout(() => {
         clearInterval(timer);
         textArea.fadeIn(duration);
         testItem1.hide();
         counter.hide();
      }, 45000)

      setTimeout(() => {
         textArea.hide(duration);
         $(this).hide();
         $('#it-2-btn-3').show();
      }, 90000)
   })

   $('#it-2-btn-3').click(function() {
      const textArea = $('#test-2-textarea');
      const testItem1 = $('.test_2_item-3');
      const counter = $('.it-2-timer');
      const duration = 800;
      let str = 45;
      $(this).prop('disabled', 'true');

      counter.html(str + ' сек');
      testItem1.fadeIn();
      counter.fadeIn(duration);

      const timer = setInterval(() => counter.html((str--) - 1 + ' сек'), 1000);

      setTimeout(() => {
         clearInterval(timer);
         textArea.fadeIn(duration);
         testItem1.hide();
         counter.hide();
      }, 45000)

      setTimeout(() => {
         textArea.hide(duration);
         $(this).hide();
         $('#it-2-btn-4').show();
      }, 90000)
   })

   $('#it-2-btn-4').click(function() {
      const textArea = $('#test-2-textarea');
      const testItem1 = $('.test_2_item-4');
      const counter = $('.it-2-timer');
      const duration = 800;
      let str = 45;
      $(this).prop('disabled', 'true');

      counter.html(str + ' сек');
      testItem1.fadeIn();
      counter.fadeIn(duration);

      const timer = setInterval(() => counter.html((str--) - 1 + ' сек'), 1000);

      setTimeout(() => {
         clearInterval(timer);
         textArea.fadeIn(duration);
         testItem1.hide();
         counter.hide();
      }, 45000)

      setTimeout(() => {
         textArea.hide(duration);
         $(this).hide();
      }, 90000)
   })

   $(function () {
      contentWayPoint();
      goToTop();
      loaderPage();
      counterWayPoint();
      counter();
   });
}());