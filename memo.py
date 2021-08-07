    process-wiki)
        echo "processing ko-wikipedia..."
        mkdir -p /notebooks/embedding/data/processed
        python preprocess/dump.py --preprocess_mode wiki \
            --input_path /notebooks/embedding/data/raw/kowiki-latest-pages-articles.xml.bz2 \
            --output_path /notebooks/embedding/data/processed/processed_wiki_ko.txt
        ;;