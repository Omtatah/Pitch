jQuery(document).ready(function () {
  // Unbind on document ready so it will still at least try
  // to be functional while the page may still be loading
  sstk_gallery_custom_links_setup();

  // Do unbinding, etc. again in window.onload to help reduce
  // the number of conflicting lightboxes etc. without
  // making the user have to declare js dependencies
  function addLoadEvent( func ) {
    var oldOnload = window.onload;
    if ( typeof window.onload != 'function' ) {
      window.onload = func;
    } else {
      window.onload = function() {
        oldOnload();
        func();
      }
    }
  }
  addLoadEvent(sstk_gallery_custom_links_setup);
});

/**
 * Setup the custom links.
 */
function sstk_gallery_custom_links_setup() {
  jQuery('.no-lightbox, .no-lightbox img').off('click');
  jQuery('a.no-lightbox').click( sstk_gallery_custom_links_click );
  jQuery('a.set-target').off('click');
  jQuery('a.set-target').click( sstk_gallery_custom_links_click );
}

/**
 * Redirect to proper URL when custom link is clicked.
 *
 * @return {bool} False.
 */
function sstk_gallery_custom_links_click() {
  if ( !this.target || this.target == '' || this.target == '_self' ) {
    window.location = this.href;
  } else {
    window.open( this.href, this.target );
  }

  return false;
}
