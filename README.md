# Documenters.org
In the Winter 2020 Knight Lab Studio, we undertook a project we called ["Speed Reading Robots"](https://studio.knightlab.com/projects/documenters/), with a goal of exploring whether computational methods could help find meaning in or direct attention to documents gathered as part of the [Documenters.org](https://www.documenters.org/) web scraping process.

We explored a number of methods, including extracting structured data, topic modeling, and entity analysis.  

This repository includes a variety of code scraps to that end.


## Tools

Recreate the DocumentCloud documents database

```
 $ rm data/DocumentCloud/db.json
 $ python -m tools.makedb data/DocumentCloud/documents.json data/DocumentCloud/db.json
```

Fetch OCR docs from DocumentCloud

```
 $ python -m tools.fetchdocs [-v]
```
## Exploring the data

See [Getting started with the data](https://github.com/NUKnightLab/Documenters.org/blob/master/EXPLORATIONS.md#getting-started-with-the-data) in the Explorations doc.

## From the project one-sheet

[Project one-sheet (private link)](https://docs.google.com/document/d/1JXfXJ9TPhkUZ6f3gySFPUIMTfm31S_iln7bCOOkq5bw/edit#)

### Description

Local governments hold a lot of meetings which are meant to allow the public to observe and comment on policy and legislation.  But local news organizations are cutting back and often can’t cover them. Chicago’s City Bureau has developed a program called Documenters, which trains citizens and pays them to cover those meetings. Along the way, they have developed software which grabs not just the schedule of these meetings but the agendas, handouts, and other documents -- documents which may have important information about future plans and laws, but which usually go unread.

What if we could make software which reads the documents for us, looking for patterns or telling humans which ones are worth their time?  For this project, we’ll work closely with City Bureau to take advantage of their system for collecting the documents, and their knowledge of public meetings and processes. Together, we’ll look for the “signal in the noise”. We’re hoping to build a mixed team including coders with at least a little experience in natural language and document analysis, as well as people who are interested in civics and government, who can help identify what’s interesting and think about how humans would be best served by any software we might create.

### Questions

What information can be pulled from local government records?
Are there notable trends in local government records? Do they cut across types of agencies or jurisdictions?
How can text analysis/machine learning be used to augment capacity in smaller newsrooms?

### Milestones

 * [Weeks 1-2](https://github.com/NUKnightLab/Documenters.org/milestone/1): Meet with City Bureau, learn about meetings and documents; work with journalists and activists to begin developing questions about what’s in the documents; initial experiments with writing programs to analyze documents.
 * [Weeks 3-5](https://github.com/NUKnightLab/Documenters.org/milestone/2): Go deeper on software-based document analysis; generalize interviews with specialists into one or more personas who need a way to make use of information discovered by the software. Generate ideas for an effective interface for those people to make use of information.
 * [Weeks 6-8](https://github.com/NUKnightLab/Documenters.org/milestone/3): Further iteration on analysis software; further iteration on user interface for analysis
 * [Weeks 9-10](https://github.com/NUKnightLab/Documenters.org/milestone/4): Write up the project; work with City Bureau to transfer knowledge for ongoing development.

### Links, Readings

 * City Bureau [Documenters Field Guide](https://fieldguide.documenters.org/)
 * Nieman Lab [Local public meetings are a scrape and a tap away, on City Bureau’s Documenters tool](https://www.niemanlab.org/2019/01/local-public-meetings-are-a-scrape-and-a-tap-away-on-city-bureaus-documenters-app/)
 * Quartz [How Quartz used AI to help reporters search the Mauritius Leaks](https://qz.com/1670632/how-quartz-used-ai-to-help-reporters-search-the-mauritius-leaks/)
 * Quartz AI Studio [Helping Journalists use Machine Learning](https://qz.ai/)
 * DocumentCloud [documents collected by City Bureau’s scrapers](https://www.documentcloud.org/public/search/Account:21089-documenters-app)
 * City Bureau's github [city-scrapers](https://github.com/city-bureau/city-scrapers)

### Outcome

Students who join this project will help solve real world problems about how journalists and citizens monitor government. They will also get a better understanding of how city governments really function. And they’ll help City Bureau chart a path forward for helping journalists and citizens in Chicago and other Documenters cities to better understand and get involved in local civic life.
