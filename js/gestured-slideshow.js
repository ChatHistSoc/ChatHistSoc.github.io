/*
	By Osvaldas Valutis, www.osvaldas.info
	Available for use under the MIT License
*/

$( document ).ready( function()
{
	(function( $ )
	{
		$.fn.gesturedSlideshow = function()
		{
			var stack = this,
				inMotion,
				ratio,
				film,
				filmPos,
				filmWidth,
				containerWidth,

				setFilms = function()
				{
					stack.find( 'ul' ).each( function()
					{
						var width = 0;
						$( this ).find( 'li' ).each( function() { width += $( this ).outerWidth() + parseInt( $( this ).css( 'margin-left' ) ) + parseInt( $( this ).css( 'margin-right' ) ); });
						$( this ).stop( true, true ).width( width ).animate( { 'left': ( $( this ).parent().width() - width ) / 2 + 'px' }, 500 );
					});
				},

				start = function( impulse )
				{
					if( containerWidth > filmWidth ) return false;
					inMotion = true;
					filmPos  = parseInt( film.css( 'left' ) );
					ratio	  = filmWidth / containerWidth;
					film.stop( true, true ).animate( { 'left' : filmPos + ( ratio * ( ( containerWidth / 2 ) - impulse ) ) + 'px' }, 250 );
				},

				move = function( impulse )
				{
					if( containerWidth > filmWidth ) return false;
					if( inMotion ) { setTimeout( function() { inMotion = false; }, 250 ); return false; }
					film.stop( true, true ).css( { 'left' : filmPos + ( ratio * ( ( containerWidth / 2 ) - impulse ) ) + 'px' } );
				},

				end = function()
				{
					if( containerWidth > filmWidth ) return false;
					film.stop( true, true ).animate( { 'left' : ( containerWidth - filmWidth ) / 2 + 'px' }, 500 );
				};

			setFilms();
			$( window ).resize( setFilms );

			stack
			.bind( 'mouseenter touchstart',	function()		{ containerWidth = $( this ).width(); film = $( this ).find( 'ul' ); filmWidth = film.width(); } )
			.bind( 'mouseenter',			function( e )	{ start( e.pageX ); } )
			.bind( 'touchstart',			function( e )	{ start( e.originalEvent.touches[0].pageX ); e.preventDefault(); } )
			.bind( 'mousemove',				function( e )	{ move( e.pageX ); } )
			.bind( 'touchmove',				function( e )	{ move( e.originalEvent.touches[0].pageX ); } )
			.bind( 'mouseleave touchend',	end );
		};
	})( jQuery );
});