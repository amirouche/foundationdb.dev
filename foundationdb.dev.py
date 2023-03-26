from pathlib import Path
from subprocess import run
from lxml.html import fromstring as string2html
import shlex
from datetime import datetime
from feedgen.feed import FeedGenerator
import pytz


def render(root, path):
    print('** reading {}'.format(path))
    directory = path.parent
    command = 'pandoc --from=markdown+yaml_metadata_block --mathml --standalone {} --template={} --output={}'
    command = command.format(path, root / 'template.html', directory / 'index.html')
    run(shlex.split(command))

def read(path):
    print('** reading {}'.format(path))
    with path.open('r') as f:
        html = f.read()
    html = string2html(html)
    try:
        title = html.xpath("/html/head/meta[@key='title']/@value")[0]
        date = html.xpath("/html/head/meta[@key='date']/@value")[0]
        abstract = html.xpath("/html/head/meta[@key='abstract']/@value")[0]
        date = datetime.fromisoformat(date)
        date = date.replace(tzinfo=pytz.UTC)
        return path, title, date, abstract
    except Exception:
        print("Ignoring '{}' failed to gather metadata!".format(path))
        return path, None, None, None

def main():
    print('* converting md to html')
    root = Path('.')
    for path in root.rglob('**/index.md'):
        if str(path).startswith('.'):
            continue
        path = path.resolve()
        render(root, path)
    print('* gathering metadata')
    meta = []
    for path in root.rglob('**/index.html'):
        if str(path).startswith('.'):
            continue
        if str(path) == 'index.html':
            continue
        meta.append(read(path))
    meta.sort(key=lambda x: x[2], reverse=True)

    with open('header.md') as f:
        out = f.read()

    for path, title, date, abstract in meta:
        out += "> ## [{}](/{})\n>{}\n>\n> {}\n\n".format(title, path, date.strftime("%Y-%m-%d"), abstract)

    print('* Creating index')
    with open('index.md', 'w') as f:
        f.write(out)
    render(root, Path('index.md').resolve())

    print('* Creating feeds')

    fg = FeedGenerator()
    fg.id('https://foundationdb.dev')
    fg.title('FoundationDB.dev')
    
    fg.link( href='https://foundationdb.dev', rel='alternate' )
    fg.subtitle('The easy distributed database!')
    fg.language('en')

    for path, title, date, abstract in meta:
        fe = fg.add_entry()
        url = 'https://foundationdb.dev/{}'.format(path)
        fe.id(url)
        fe.guid(url, permalink=True)        
        fe.title(title)
        fe.link(href=url)
        fe.summary(abstract)
        fe.description(abstract)        
        fe.published(date)
    fg.atom_file('atom.xml')
    fg.rss_file('rss.xml')

    
if __name__ == '__main__':
    main()
