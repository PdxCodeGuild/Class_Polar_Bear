
# Lab 4: Animations

We are going to practice with animations by recreating several animated buttons.
To start, copy the following html and css as your starting point.

#### HTML
```html
  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Animations</title>
 
</head>
<body>
  <div class="main wrapper">
    <h1>Simple button effects</h1>
  </div>

  <section>
    <div class="btn-1Wrapper wrapper">
      <div class="btn">Hover on Me</div>
    </div>

    <div class="btn-2Wrapper wrapper">
      <div class="btn">Hover on Me</div>
    </div>

    <div  class="btn-3Wrapper wrapper">
      <div class="btn">Hover on Me</div>
    </div>

      <div class="btn-4Wrapper wrapper">
      <div class="btn">Click Me</div>
    </div>

    <div  class="btn-5Wrapper wrapper">
      <div class="btn">Hover on Me</div>
    </div>

    <div class="btn-6Wrapper wrapper">
      <div class="btn">Click Me</div>
    </div>

    <div class="btn-7Wrapper wrapper">
      <div class="btn">Hover on Me</div>
    </div>

    <div class="btn-8Wrapper wrapper">
      <div class="btn">Hover on Me</div>
    </div>

    <div class="btn-9Wrapper wrapper">
      <div class="btn">Hover on Me</div>
    </div>

    <div class="btn-10Wrapper wrapper">
      <div class="btn">Hover on Me</div>
    </div>

    <div class="btn-11Wrapper wrapper">
      <div class="btn">Hover on Me</div>
    </div>

    <div class="btn-12Wrapper wrapper">
      <div class="btn">Hover on Me</div>
    </div>
  </section>
</body>
</html>
```
#### CSS
```css
@import url('https://fonts.googleapis.com/css?family=Dosis:400,600');

body, html {
	height: 100%;
	font-family: 'Dosis', sans-serif;
	color: #fff;
	margin: 0;
}

.btn {
	font-size:20px;
	background-color:#fff;
	padding:20px;
	color:#333;
	border-radius: 20px;
}

.wrapper:not(.main) {
	width: 24%;
}

h1 {
	margin:0;
}

.wrapper {
	height:50vh;
	display:flex;
	align-items:center;
	justify-content:center;
	min-height:250px;
	flex-direction:column;
	background:#00A5CF;
	border:solid 0.5px;
}

section {
	display:flex;
	flex-wrap:wrap;
	justify-content:center;
	margin:30px 0;
}

.main {
	background-color: #E94F37;
	padding-top: 20px;
}

```

We will replicate the buttons found on this [codepen](https://codepen.io/Chelsea-Dover/full/ygNwej/).