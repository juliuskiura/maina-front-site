function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');


var priceUrl = "/products/price/"


var form = document.querySelector('.product-query')
$(form).submit(function(e) {
  e.preventDefault();
 
  var studyLevelValue = document.getElementById('id_study_level').value
  var serviceCategoryValue = document.getElementById('id_service_category').value
  var assignmentTypeValue = document.getElementById('id_assignment_type').value
  var turnaroundValue = document.getElementById('id_turnaround').value
  var numpages = document.getElementById('id_numpages').value

 const data = {'study_level':studyLevelValue, 'service_category':serviceCategoryValue, 'assignment_type':assignmentTypeValue, 'turnaround':turnaroundValue, 'numpages': numpages}

 fetch(priceUrl, {
  method: 'POST',
  headers: {
      'Content_type':'application/json',
      'x-CSRFToken':csrftoken,
  },
  body: JSON.stringify(data)
}).then((response)=>{
  return response.json()
}).then((data)=>{
  get_price(data)
})

})



function get_price(response) {
  
var amount_p =document.querySelector('.total_am')
amount_p.innerHTML=''
var order_button =document.querySelector('#order_btn')
const para = document.createElement("p");
para.classList.add('amount')
para.innerHTML = "Total: $"+response.total;
amount_p.appendChild(para);
order_button.classList.remove('d-none')

}






var subscribeForm = document.getElementById('subscribeForm')

subscribeForm.addEventListener('submit', event => {
  event.preventDefault();
  email = document.getElementById('id_email').value;
  console.log('this-emai:', email)
  subsUrl = '/contact/subscribe/'
  
 const data = {'email':email}
  fetch(subsUrl, {
    method: 'POST',
    headers: {
        'Content-type':'application/json',
        'x-CSRFToken':csrftoken,
    },
    body: JSON.stringify(data)
  }).then((response)=>{
    return response.json()
  }).then((data)=>{    
    let parentForm = document.querySelector('.subs-div')
    
    parentForm.innerHTML =  `<div class="alert alert-warning alert-dismissible fade show" role="alert">
    <strong>${data['data']}!</strong> 
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>`
    

    console.log(data)
  })
});

const ArrayblogCta = document.getElementsByClassName('blog-cta')
// // const ArrayblogCta = Array.from(document.querySelectorAll('.blog-cta'))

for (let index = 0; index < ArrayblogCta.length; index++) {
  const element = ArrayblogCta[index];
  console.log(element)
  const ParentblogCTA = document.createElement('div')
  const ctaButton = document.createElement('a')
  ctaButton.className='btn-cta-blog'
  ctaButton.setAttribute('href', 'https://appnursing.cannyva.com/customer/register/')
  ctaButton.setAttribute('target', '_blank')
  ctaButton.innerHTML ='Sign up & Order'  

  ParentblogCTA.className ='blog-cta-container'
  element.parentNode.insertBefore(ParentblogCTA, element);
  ParentblogCTA.appendChild(element)
  ParentblogCTA.appendChild(ctaButton)
}
