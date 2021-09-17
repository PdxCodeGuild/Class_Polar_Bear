# HTML

## Random notes
- Shorcut to comment ctrl + /

## Headings

- h1-h6

## Inline

- Inline elements go inside block elements
- Can surround a specific part of a bigger element

```
<h1>Hello world!</h1>
<h2>Hello world!</h2>
<h3>Hello world!</h3>
<h4>Hello world!</h4>
<h5>Hello world!</h5>
<h6>Hello world!</h6>
```
## Paragraphs

```
<p>This is a paragraph</p>
```

## Links

### Anchor tag
- Href links to link or page

```
<a href="google.com">Google</a>
```
- Takes you to google

## Lists

### Ordered - Usually has numbers

```
<ol>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ol>
```
### Unordered - Bullet points
```
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```
## Break

```
hello
<br>
breaking....
<br>
done breaking...
```
## Images

- Self closing
- 2 required attributes
    - src = link to image
    - alt = text to represent img in case broken
- extra attributes
    - height
    - width
    - when choosing just 1 of these, img will scale on its' own

```
<img src="https://picsum.photos/200/300" alt="random img">
```

## Tables

- th will be a heading
- multiple will create a row of headings
- tr will create a row
- td elements are elements that will go in the row

```
<table>
    <thead>
        <th>States1</th>
        <th>States2</th>
        <th>States3</th>
    </thead>
    <tbody>
        <tr>
            <td>New York</td>
            <td>Massachussetts</td>
            <td>Connecticut</td>
        </tr>
    </tbody>                    
</table>
```