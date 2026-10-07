# GreyScript Prime

<span class="gh-badge">Development</span> <span class="gh-badge">SDK</span>

**GreyScript Prime** is a helper library (SDK) that adds convenient methods for working with text, numbers, lists, maps, and files. Several other tools, including [Airlink](airlink.md), are built on top of it.

<table class="gh-meta"><tbody>
<tr><td>Author</td><td>Svarii</td></tr>
<tr><td>Repository</td><td><a href="https://github.com/Svarii/greyscript-prime">github.com/Svarii/greyscript-prime</a></td></tr>
<tr><td>License</td><td>MIT</td></tr>
</tbody></table>

## What it provides

| Category | Examples |
|---|---|
| TextMesh Pro methods | `.color()`, `.bold()`, alignment, sizing |
| Number methods | `.clamp()`, `.lerp()`, randomisation |
| List methods | manipulation helpers |
| Map methods | attribute helpers |
| File management | create, delete, exists, append |

Methods are called directly on objects, e.g. `myString.color("red")` or `myNumber.clamp(0, 10)`.

## Setup

Clone the repository and open it in VS Code with the recommended extensions ([Greybel VS](greybel-vs.md), Markdown Preview Enhanced, PlantUML). Import the library in your project and call its methods on your objects.
