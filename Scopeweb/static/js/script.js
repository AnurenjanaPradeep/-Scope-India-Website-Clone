          <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
     
$('#id_country').change(function(){
    var country_name = $(this).val();

    $.ajax({
        url: "{% url 'get_states' %}",
        data: {'country': country_name},
        success: function(data){
            var state_select = $('#id_state');
            
            state_select.append('<option value="">Select State</option>');

            $.each(data.states, function(index, state){
                state_select.append(
                    '<option value="' + state.state_name + '">' + state.state_name + '</option>'
                );
            });
        }
    });
});
$('#id_state').change(function(){
    var state_name=$(this).val();
    $.ajax({
        url:"{%url 'get_city' %}",
        data:{'state':state_name},
        success:function(data){
            var city_select=$('#id_city');
            
            city_select.append('<option value="">Select City</option>');
             $.each(data.city, function(index, city){
                city_select.append('<option value="' + city.city_name + '">' + city.city_name + '</option>')
             }
             )

        }
    })
})

