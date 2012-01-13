function channels(network){

    var url ="/get_channels/" + network;

    $.get(url, function(data){
	    $( "#channels_list" ).empty().append(data);
	}
	);
}
function programs(channel){

    var url ="/get_programs/" + channel;

    $.get(url, function(data){
	    $( "#programs_list" ).empty().append(data);
	}
	);
}
function videos(program){

    var url ="/get_videos/" + program;

        $.get(url, function(data){
    	    $( "#videos_list" ).empty().append(data);
    	}
    	);
}

function video(program_name, episode_number){
    var url="/episode/" + program_name + "/" + episode_number;
    $.get(url, function(data){
	    $( "#video").empty().append(data);
	}
	);
}
